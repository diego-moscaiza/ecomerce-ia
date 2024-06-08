import { defineConfig } from "astro/config";
import tailwind from "@astrojs/tailwind";
import node from "@astrojs/node";

// https://astro.build/config
export default defineConfig({
  vite: {
    allowInlining: true
  },
  prefetch: {
    defaultStrategy: "viewport"
  },
  integrations: [tailwind()],
  image: {
    remotePatterns: [{
      protocol: "https"
    }]
  },
  output: "server",
  adapter: node({
    mode: "middleware"
  })
});