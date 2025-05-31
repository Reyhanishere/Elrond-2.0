/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html",
  './templates/**/*.html',
  './**/*.html',
  './static/js/**/*.js',
],

    safelist: [
    "button",
    "primary",
    "secondary",
    "danger",
    "EasyMDEContainer",
    "error",
    "allauth-form",
  ],
  theme: {
    extend: {
      boxShadow: {
        underline : "inset 0 -2px 0 0"
      }
    },
  },
  plugins: [
    require("@tailwindcss/forms"),
    require("@tailwindcss/typography"),
  ],
}

