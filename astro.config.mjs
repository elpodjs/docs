import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";

export default defineConfig({
  site: "https://elpod.vercel.app",
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
