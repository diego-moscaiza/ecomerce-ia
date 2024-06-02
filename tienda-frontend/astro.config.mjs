import { defineConfig } from "astro/config";
import tailwind from "@astrojs/tailwind";
import node from "@astrojs/node";

import auth from "auth-astro";

// https://astro.build/config
export default defineConfig({
  vite: {
    allowInlining: true
  },
  prefetch: {
    defaultStrategy: "viewport"
  },
  integrations: [tailwind(), auth()],
  image: {
    remotePatterns: [{
      protocol: "https"
    }]
  },
  output: "hybrid",
  adapter: node({
    mode: "standalone"
  })
});