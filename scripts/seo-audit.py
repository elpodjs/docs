"""Audit the generated Astro site with only Python's standard library."""

from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import json
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
SITE = "https://elpod.vercel.app"


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.h1 = []
        self.meta = {}
        self.canonical = []
        self.links = []
        self.json_ld = []
        self.pre_count = 0
        self.main_text = []
        self._title = self._h1 = self._json = self._main = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "title":
            self._title = True
        elif tag == "h1":
            self._h1 = True
            self.h1.append("")
        elif tag == "main":
            self._main = True
        elif tag == "meta":
            self.meta[attrs.get("name") or attrs.get("property")] = attrs.get("content", "")
        elif tag == "link" and attrs.get("rel") == "canonical":
            self.canonical.append(attrs.get("href", ""))
        elif tag == "a":
            self.links.append(attrs.get("href", ""))
        elif tag == "pre":
            self.pre_count += 1
        elif tag == "script" and attrs.get("type") == "application/ld+json":
            self._json = True
            self.json_ld.append("")

    def handle_endtag(self, tag):
        if tag == "title":
            self._title = False
        elif tag == "h1":
            self._h1 = False
        elif tag == "main":
            self._main = False
        elif tag == "script":
            self._json = False

    def handle_data(self, data):
        if self._title:
            self.title += data
        if self._h1:
            self.h1[-1] += data
        if self._json:
            self.json_ld[-1] += data
        if self._main:
            self.main_text.append(data)


def file_for(path):
    path = urlparse(path).path
    if path == "/":
        return DIST / "index.html"
    if Path(path).suffix:
        return DIST / path.lstrip("/")
    return DIST / path.lstrip("/") / "index.html"


def main():
    pages = {}
    errors = []
    html_files = sorted(DIST.rglob("*.html"))
    for html in html_files:
        page = Page()
        page.feed(html.read_text())
        path = "/" if html == DIST / "index.html" else "/" + html.relative_to(DIST).parent.as_posix() + "/"
        pages[path] = page
        if not page.title:
            errors.append(f"{path}: missing title")
        if len(page.h1) != 1 or not page.h1[0].strip():
            errors.append(f"{path}: expected one nonempty H1, got {len(page.h1)}")
        for key in ("description", "og:title", "og:description", "og:image", "og:url", "twitter:card", "twitter:title", "twitter:description", "twitter:image"):
            if not page.meta.get(key):
                errors.append(f"{path}: missing {key}")
        if page.canonical != [SITE + path]:
            errors.append(f"{path}: incorrect canonical {page.canonical}")
        if not page.json_ld:
            errors.append(f"{path}: missing JSON-LD")
        for block in page.json_ld:
            try:
                data = json.loads(block)
                assert isinstance(data, list) and all("@type" in item for item in data)
            except (ValueError, AssertionError):
                errors.append(f"{path}: invalid JSON-LD")
        if path.startswith("/docs/") and len(" ".join(page.main_text).split()) < 100:
            errors.append(f"{path}: very little raw HTML text")

    for field, values in (("title", [p.title for p in pages.values()]), ("description", [p.meta.get("description") for p in pages.values()])):
        for value, count in Counter(values).items():
            if value and count > 1:
                errors.append(f"duplicate {field}: {value}")

    inbound = Counter()
    for source, page in pages.items():
        for href in page.links:
            if not href.startswith("/") or href.startswith("//"):
                continue
            target = urlparse(href).path
            if not file_for(target).exists():
                errors.append(f"{source}: broken internal link {href}")
            if target in pages and target != source:
                inbound[target] += 1
    for path in pages:
        if path != "/" and inbound[path] == 0:
            errors.append(f"{path}: no inbound HTML links")

    sitemap_index = DIST / "sitemap-index.xml"
    if not sitemap_index.exists():
        errors.append("missing sitemap index")
    else:
        listed = set()
        for sitemap in DIST.glob("sitemap-*.xml"):
            if sitemap.name == "sitemap-index.xml":
                continue
            for loc in ET.parse(sitemap).iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc"):
                listed.add(urlparse(loc.text).path)
        for path in pages:
            if path not in listed:
                errors.append(f"{path}: absent from sitemap")
    if not (DIST / "robots.txt").exists():
        errors.append("missing robots.txt")
    if not (DIST / "llms.txt").exists():
        errors.append("missing llms.txt")

    print(f"Audited {len(pages)} generated HTML pages; {sum(p.pre_count for p in pages.values())} raw HTML code blocks.")
    print(f"Issues: {len(errors)}")
    for error in errors:
        print("- " + error)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
