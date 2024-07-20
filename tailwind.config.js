/** @type {import('tailwindcss').Config} */
const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
  content: [
    './layouts/**/*.html',
    './content/**/*.md',
    './themes/**/*.{html,md}',
  ],
  theme: {
    extend: {
      backgroundImage: {
        "landing-top-img": "url('/images/landing-top-bg.svg')",
        "empower-trust": "url('/images/bg-empowering-trust.svg')",
      },
      boxShadow: {
        'top-left-to-bottom-right': '1px 1px 1px 1px rgba(63,65,83, 0.5), 1px 1px 1px 1px rgba(140,144,185, 1)',
        'single-footer-shadow': '0px -30px 20px rgba(132, 132, 132, 0.11)',
        "get-pac": "0px 0px 40px rgba(89, 64, 246, 0.3)"
      },
      fontFamily: {
        'sans': ['"Inter"','sans-serif', ...defaultTheme.fontFamily.sans],
      },
    },
    colors: {
      "light-bg-to": "#F3F3F3",
      "light-text-blue": "#131440",
    },
    container: {
      padding: "10px"
    }
  },
  plugins: [
    require('daisyui'),
    require('@tailwindcss/typography'),
  ],
  darkMode: "selector",
}
