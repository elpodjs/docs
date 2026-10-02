import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";

export default defineConfig({
  site: "https://github.com/acefolioDev/elpod",
  output: "static",
  trailingSlash: "always",
  integrations: [sitemap()],
  build: { inlineStylesheets: "auto" },
  vite: {
    optimizeDeps: {
      include: ["gsap", "gsap/ScrollTrigger"],
    },
  },
});
