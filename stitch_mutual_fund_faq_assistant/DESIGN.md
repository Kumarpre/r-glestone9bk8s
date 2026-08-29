---
name: Lumina Finance
colors:
  surface: '#0b1326'
  surface-dim: '#0b1326'
  surface-bright: '#31394d'
  surface-container-lowest: '#060e20'
  surface-container-low: '#131b2e'
  surface-container: '#171f33'
  surface-container-high: '#222a3d'
  surface-container-highest: '#2d3449'
  on-surface: '#dae2fd'
  on-surface-variant: '#c2c6d6'
  inverse-surface: '#dae2fd'
  inverse-on-surface: '#283044'
  outline: '#8c909f'
  outline-variant: '#424754'
  surface-tint: '#adc6ff'
  primary: '#adc6ff'
  on-primary: '#002e6a'
  primary-container: '#4d8eff'
  on-primary-container: '#00285d'
  inverse-primary: '#005ac2'
  secondary: '#4edea3'
  on-secondary: '#003824'
  secondary-container: '#00a572'
  on-secondary-container: '#00311f'
  tertiary: '#ffb786'
  on-tertiary: '#502400'
  tertiary-container: '#df7412'
  on-tertiary-container: '#461f00'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d8e2ff'
  primary-fixed-dim: '#adc6ff'
  on-primary-fixed: '#001a42'
  on-primary-fixed-variant: '#004395'
  secondary-fixed: '#6ffbbe'
  secondary-fixed-dim: '#4edea3'
  on-secondary-fixed: '#002113'
  on-secondary-fixed-variant: '#005236'
  tertiary-fixed: '#ffdcc6'
  tertiary-fixed-dim: '#ffb786'
  on-tertiary-fixed: '#311400'
  on-tertiary-fixed-variant: '#723600'
  background: '#0b1326'
  on-background: '#dae2fd'
  surface-variant: '#2d3449'
typography:
  display-lg:
    fontFamily: Outfit
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Outfit
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Outfit
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Outfit
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.02em
  code-mono:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-padding: 24px
  gutter: 16px
  margin-mobile: 16px
  margin-desktop: 64px
  max-width: 1200px
---

## Brand & Style

The design system is engineered for a premium fintech experience, specifically tailored for a Mutual Fund FAQ Assistant. The brand personality is **technologically advanced, authoritative, and ultra-modern**. It aims to evoke a sense of digital craftsmanship and "financial clarity" through a sophisticated **Dark Mode Glassmorphism** aesthetic.

The target audience consists of discerning investors who value precision and speed. The UI utilizes depth, light, and transparency to simulate a high-end physical interface. Visual hierarchy is established through "light-source" logic, where active elements appear to glow or catch a subtle edge light, reinforcing the product's role as an intelligent, illuminating assistant in the complex world of finance.

## Colors

The palette is anchored by a deep **Slate/Charcoal (#0f172a)** base to provide a sense of stability and premium quality. 

- **Primary Action:** Electric Blue (#3b82f6) is used for the most critical interactions and the AI's "active" state.
- **Secondary/Success:** Emerald Green (#10b981) denotes positive market trends, completed actions, and "verified" fund data.
- **Surface Strategy:** Backgrounds are not flat; they utilize subtle radial gradients to create a sense of a light source behind the "glass" panels.
- **Functional Accents:** Border glows and backdrop blurs use low-opacity versions of the primary blue to create a "halo" effect around interactive containers.

## Typography

This design system uses a dual-font strategy to balance character with utility. 

**Outfit** is used for headings and display text. Its geometric precision and wide apertures feel modern and tech-forward. High-level numbers (like fund returns) should always use Outfit for maximum impact.

**Inter** is the workhorse for body copy, assistant responses, and labels. Its exceptional legibility ensures that complex financial explanations remain readable even on small screens. 

- Use `display-lg` for welcome screens or major assistant prompts.
- Use `label-md` with 2% letter spacing for category tags or metadata.
- Ensure all body text maintains a minimum contrast ratio of 7:1 against the dark glass backgrounds.

## Layout & Spacing

The layout follows a **Fluid-Fixed Hybrid** model. While the overall container has a maximum width for readability on large monitors, the internal components utilize a flexible grid to accommodate the conversational nature of the assistant.

- **Grid:** A 12-column grid is used for dashboard layouts, while the assistant chat interface follows a centered 8-column column for focus.
- **Rhythm:** Spacing follows a strict 8px base unit. 
- **Breathing Room:** Because the dark mode uses glassmorphism, ample white space (or "dark space") is required to prevent the UI from feeling cluttered. Use `24px` (3 units) for standard padding inside glass containers.
- **Mobile:** Margins shrink to 16px, and multi-column data cards stack vertically to maintain legibility.

## Elevation & Depth

Depth is the defining characteristic of this design system. It is achieved through **Backdrop Filtration** rather than traditional drop shadows.

1.  **Level 0 (Background):** Solid `#0f172a` with a faint radial gradient (Primary Color at 5% opacity) in the top-right corner.
2.  **Level 1 (Panels):** Semi-transparent surfaces using `backdrop-filter: blur(20px)` and a 1px border of `rgba(255, 255, 255, 0.1)`. 
3.  **Level 2 (Floating/Active):** These elements use a secondary "inner glow" border. The top border is slightly brighter (`rgba(255, 255, 255, 0.2)`) to simulate top-down lighting.
4.  **Assistant Interaction:** The AI's responses occupy a unique elevation, featuring a subtle outer glow of the primary blue (#3b82f6) to differentiate its messages from user queries.

## Shapes

The shape language is **Soft & Polished**. 

- **Containers:** Main panels and card surfaces use a `1rem` (16px) radius to feel friendly and modern.
- **Interactive Elements:** Buttons and input fields use a `0.75rem` (12px) radius.
- **Avatars/Icons:** Small icons or status indicators (like "Live" market signals) are fully rounded (pill-shaped).

The consistency of the 16px radius across the layout ensures that the "glass" panels feel like a cohesive set of lenses layered over the data.

## Components

### Buttons
- **Primary:** Solid Electric Blue (#3b82f6) with a white label. Includes a 10px outer glow on hover.
- **Secondary:** Transparent with a 1px border in #3b82f6. On hover, the background fills with a 10% opacity blue.

### Input Fields (The "Ask" Bar)
The main interaction point for the FAQ Assistant. It should be a large, floating glass bar with a `backdrop-filter: blur(30px)`. The border should pulse slightly with the primary color when the AI is "thinking."

### Assistant Response Cards
These cards use the secondary color (#10b981) for success indicators (e.g., "Yield is up"). Data visualizations within these cards (sparklines, charts) should be simplified and use the same neon accent colors.

### Chips
Used for suggested FAQs. These should be low-contrast glass elements that become solid blue with a "pop" animation when tapped.

### Micro-animations
- **Transitions:** Use a "Spring" preset (stiffness: 300, damping: 30) for cards appearing in the chat flow.
- **Glows:** Pulsating opacity (0.4 to 0.8) on the borders of active fund highlights.