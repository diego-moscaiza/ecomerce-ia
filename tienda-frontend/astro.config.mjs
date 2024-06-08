import tailwind from "@astrojs/tailwind";
import vercel from "@astrojs/vercel/serverless";
import { defineConfig } from "astro/config";

// https://astro.build/config
export default defineConfig({
  vite: {
    allowInlining: true,
  },
  prefetch: {
    defaultStrategy: "viewport",
  },
  integrations: [tailwind()],
  image: {
    remotePatterns: [
      {
        protocol: "https",
      },
    ],
  },
  output: "server",
  adapter: vercel({
    imageService: true,
  }),
});
