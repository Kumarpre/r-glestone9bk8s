/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: "class",
  theme: {
    extend: {
      "colors": {
              "inverse-primary": "#005ac2",
              "tertiary-container": "#df7412",
              "outline": "#8c909f",
              "secondary": "#4edea3",
              "secondary-fixed": "#6ffbbe",
              "on-error": "#690005",
              "on-primary-fixed": "#001a42",
              "surface-bright": "#31394d",
              "secondary-fixed-dim": "#4edea3",
              "primary": "#adc6ff",
              "primary-container": "#4d8eff",
              "surface-container-high": "#222a3d",
              "surface-tint": "#adc6ff",
              "tertiary-fixed": "#ffdcc6",
              "on-tertiary": "#502400",
              "surface": "#0b1326",
              "on-background": "#dae2fd",
              "on-secondary-fixed": "#002113",
              "outline-variant": "#424754",
              "on-surface": "#dae2fd",
              "on-secondary-container": "#00311f",
              "on-tertiary-fixed-variant": "#723600",
              "on-primary-fixed-variant": "#004395",
              "tertiary-fixed-dim": "#ffb786",
              "inverse-on-surface": "#283044",
              "on-primary": "#002e6a",
              "secondary-container": "#00a572",
              "on-error-container": "#ffdad6",
              "tertiary": "#ffb786",
              "surface-container-low": "#131b2e",
              "on-tertiary-fixed": "#311400",
              "primary-fixed": "#d8e2ff",
              "error-container": "#93000a",
              "surface-container": "#171f33",
              "inverse-surface": "#dae2fd",
              "surface-container-highest": "#2d3449",
              "primary-fixed-dim": "#adc6ff",
              "surface-container-lowest": "#060e20",
              "on-secondary": "#003824",
              "on-secondary-fixed-variant": "#005236",
              "surface-dim": "#0b1326",
              "error": "#ffb4ab",
              "on-primary-container": "#00285d",
              "background": "#0b1326",
              "on-tertiary-container": "#461f00",
              "on-surface-variant": "#c2c6d6",
              "surface-variant": "#2d3449"
      },
      "borderRadius": {
              "DEFAULT": "0.25rem",
              "lg": "0.5rem",
              "xl": "0.75rem",
              "full": "9999px"
      },
      "spacing": {
              "unit": "8px",
              "max-width": "1200px",
              "gutter": "16px",
              "container-padding": "24px",
              "margin-mobile": "16px",
              "margin-desktop": "64px"
      },
      "fontFamily": {
              "label-md": [
                      "Inter"
              ],
              "body-md": [
                      "Inter"
              ],
              "code-mono": [
                      "JetBrains Mono"
              ],
              "headline-lg-mobile": [
                      "Outfit"
              ],
              "headline-md": [
                      "Outfit"
              ],
              "headline-lg": [
                      "Outfit"
              ],
              "body-lg": [
                      "Inter"
              ],
              "display-lg": [
                      "Outfit"
              ]
      },
      "fontSize": {
              "label-md": [
                      "14px",
                      {
                              "lineHeight": "1",
                              "letterSpacing": "0.02em",
                              "fontWeight": "500"
                      }
              ],
              "body-md": [
                      "16px",
                      {
                              "lineHeight": "1.5",
                              "fontWeight": "400"
                      }
              ],
              "code-mono": [
                      "14px",
                      {
                              "lineHeight": "1.5",
                              "fontWeight": "400"
                      }
              ],
              "headline-lg-mobile": [
                      "24px",
                      {
                              "lineHeight": "1.2",
                              "fontWeight": "600"
                      }
              ],
              "headline-md": [
                      "24px",
                      {
                              "lineHeight": "1.3",
                              "fontWeight": "500"
                      }
              ],
              "headline-lg": [
                      "32px",
                      {
                              "lineHeight": "1.2",
                              "letterSpacing": "-0.01em",
                              "fontWeight": "600"
                      }
              ],
              "body-lg": [
                      "18px",
                      {
                              "lineHeight": "1.6",
                              "fontWeight": "400"
                      }
              ],
              "display-lg": [
                      "48px",
                      {
                              "lineHeight": "1.1",
                              "letterSpacing": "-0.02em",
                              "fontWeight": "600"
                      }
              ]
      }
    }
  }
}
