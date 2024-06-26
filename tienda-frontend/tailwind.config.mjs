/** @type {import('tailwindcss').Config} */
export default {
  content: {
    files: [
      "./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}",
      "./node_modules/flowbite/**/*.js",
    ],
  },
  theme: {
    extend: {},
  },
  plugins: [require("flowbite/plugin")],
  corePlugins: {
    boxSizing: true,
  },
  darkMode: "class",
};
