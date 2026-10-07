const toggle = document.querySelector<HTMLButtonElement>('.theme-toggle');
const root = document.documentElement;

function syncTheme() {
  const dark = root.dataset.theme === 'dark';
  toggle?.setAttribute('aria-pressed', String(dark));
  toggle?.setAttribute('aria-label', `Switch to ${dark ? 'light' : 'dark'} mode`);
  const label = toggle?.querySelector<HTMLElement>('.theme-label');
  const icon = toggle?.querySelector<HTMLElement>('span[aria-hidden]');
  if (label) label.textContent = dark ? 'Light mode' : 'Dark mode';
  if (icon) icon.textContent = dark ? '☀' : '☾';
  document.querySelector('meta[name="theme-color"]')?.setAttribute('content', dark ? '#20120f' : '#fff8ed');
}

syncTheme();
toggle?.addEventListener('click', () => {
  const dark = root.dataset.theme !== 'dark';
  if (dark) root.dataset.theme = 'dark';
  else delete root.dataset.theme;
  try { localStorage.setItem('elpod-theme', dark ? 'dark' : 'light'); } catch (_) {}
  syncTheme();
});
