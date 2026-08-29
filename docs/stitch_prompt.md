# Prompt for Google Stitch (Phase 6.2 Frontend)

**Instructions for User:** Copy the text below the line and paste it directly into Google Stitch to generate the high-quality React frontend.

---

**Role:** You are an expert frontend developer and UX/UI designer. Your task is to build a modern, highly polished, premium single-page React application for a "Mutual Fund FAQ Assistant".

**Tech Stack:** React (Vite), plain CSS (or Tailwind if you prefer, but it must be fully responsive and styled).

**Design Aesthetics & Vibe:**
- **Premium & State-of-the-art:** The UI must wow the user at first glance. Use a modern color palette (e.g., sleek dark mode with vibrant neon accents or a very clean, trustworthy glassmorphism light theme).
- **Typography:** Use modern web fonts (like Inter or Outfit). 
- **Animations:** Include subtle micro-animations (e.g., smooth fade-ins for messages, hover states on buttons/chips, and a polished bouncing-dot typing indicator when the bot is loading).
- **Layout:** A clean chat-like interface centered on the screen, taking up the majority of the viewport, with a fixed header and a fixed input area at the bottom.

**Core Functional Requirements:**
1. **Header:** 
   - Title: "Mutual Fund Assistant"
   - A persistent, highly visible disclaimer badge/banner that reads: *"Facts-only. No investment advice."*
2. **Chat Area:**
   - Display a welcome message from the bot on load: *"Hi! I am the Mutual Fund FAQ Assistant. I can provide factual information about 5 HDFC schemes (Mid Cap, Small Cap, Large Cap, Gold ETF, and ELSS Tax Saver). What would you like to know?"*
   - User messages aligned to the right. Bot messages aligned to the left.
   - **URL Parsing:** The bot's messages will contain URLs. You MUST parse any `http://` or `https://` text in the bot's response into clickable anchor tags (`<a href="..." target="_blank">`).
   - **Category Tags:** The backend returns a `category` (e.g., FACTUAL, ERROR, ADVICE, OUT_OF_SCOPE). If the message has a category (and isn't the initial greeting), display it as a small, styled pill/tag attached to the bot's message bubble.
3. **Example Suggestions:**
   - Above the chat input, provide a horizontally scrollable or wrapping list of 3 suggestion chips:
     1. *"What is the expense ratio of HDFC Small Cap?"*
     2. *"Tell me the exit load for the Gold ETF."*
     3. *"Does the ELSS tax saver fund have a lock-in period?"*
   - Clicking a chip should instantly populate the input and send the message.
4. **Input Area:**
   - A text input field with placeholder: *"Ask a factual question about HDFC funds..."*
   - A Send button. Both should be disabled while the bot is loading.
   - Hitting `Enter` should submit the query.
5. **API Integration:**
   - When the user sends a message, make a `fetch` POST request to `http://localhost:8080/chat`.
   - Payload: `JSON.stringify({ query: userText })`
   - Headers: `{'Content-Type': 'application/json'}`
   - The API will return: `{ "answer": "...", "category": "FACTUAL" }`
   - Handle network errors gracefully by displaying an ERROR category message in the chat: *"Sorry, I am having trouble connecting to the server. Please make sure the backend is running on port 8080."*

Please output the complete, fully functioning React component code (`App.jsx`) and the corresponding CSS (`App.css`). Make sure the design looks incredibly premium.
