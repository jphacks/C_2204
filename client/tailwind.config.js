/** @type {import('tailwindcss').Config} */
module.exports = {
  purge: {
    content: ['./src/**/*.{js,jsx,ts,tsx}'],
    safelist: ['bg-mainBrand', 'hover:bg-mainBrandHover', 'text-lightShades'],
  },
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx}',
    './src/components/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        transparent: 'transparent',
        current: 'currentColor',
        lightShades: '#F9F9FB',
        lightAccent: '#DF7157',
        mainBrand: '#D55769',
        mainBrandHover: '#a2424f',
        darkAccent: '#EA9D8A',
        darkAccentHover: '#b67a6b',
        darkShades: '#45859B',
        darkText: '#333333',
        footerSVG: '#646464',
        twitter: '#1D9BF0',
        twitterHover: '#1A8CD8',
        iconGradientFrom: '#FFD900',
        iconGradientTo: '#2727F5',
      },
      boxShadow: {
        up: '0px -4px 5px rgba(0, 0, 0, 0.1)',
        down: '0px 4px 5px rgba(0, 0, 0, 0.2)',
      },
      maxHeight: {
        0: '0',
        '1/4': '25%',
        '1/2': '50%',
        '3/4': '75%',
        '5/6': '83.33%',
        '11/12': '91.66%',
        full: '100%',
      },
    },
  },
  plugins: [],
}
