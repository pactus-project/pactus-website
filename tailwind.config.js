/** @type {import('tailwindcss').Config} */
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
        'top-left-to-bottom-right': '1px 1px 1px 1px rgba(63,65,83, 0.5), 1px 1px 1px 1px rgba(140,144,185, 1)'
      },
    },
    colors: {
      "light-bg-to": "#F3F3F3",
      "light-text-blue": "#131440",
    }
  },
  plugins: [
    require('daisyui'),
  ],
  darkMode: "selector",
}
