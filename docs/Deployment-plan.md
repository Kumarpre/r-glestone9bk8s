# Deployment Plan

This document outlines the steps to deploy the Mutual Fund FAQ Assistant to production using Railway for the backend and Vercel for the frontend.

## 1. Prerequisites
- A GitHub repository containing the complete source code.
- An account on [Railway.app](https://railway.app/).
- An account on [Vercel.com](https://vercel.com/).
- A valid Google Gemini API Key.

---

## 2. Backend Deployment (Railway)

The backend is built with FastAPI and runs on Uvicorn. Railway can natively deploy Python applications using the `requirements.txt` file and a `Procfile` or start command.

### Steps:
1. **Prepare the App for Railway**:
   Create a `Procfile` in the root of your project directory with the following content:
   ```text
   web: uvicorn src.main:app --host 0.0.0.0 --port $PORT
   ```
2. **Link GitHub**:
   - Go to your Railway Dashboard.
   - Click **New Project** -> **Deploy from GitHub repo**.
   - Select your repository.
3. **Configure Environment Variables**:
   - Once the service is created, go to the **Variables** tab.
   - Add the following variables:
     - `GEMINI_API_KEY`: `<your_gemini_api_key>`
     - `MODEL_GENERATOR`: `gemini-2.5-flash`
     - `MODEL_CLASSIFIER`: `gemini-2.5-flash`
4. **Deploy & Get URL**:
   - Railway will automatically build and deploy your application.
   - Go to the **Settings** tab -> **Networking** and click **Generate Domain** (e.g., `mutual-fund-api.up.railway.app`).
   - Note this URL down for the frontend configuration.

---

## 3. Frontend Deployment (Vercel)

The frontend is a static React application built with Vite.

### Steps:
1. **Update API URL**:
   - In `frontend/src/App.jsx`, update the `fetch` call URL from `http://localhost:8080/chat` to your Railway production URL (e.g., `https://mutual-fund-api.up.railway.app/chat`).
   *(Alternatively, you can configure an environment variable in Vite like `VITE_API_URL`)*
2. **Link GitHub**:
   - Go to your Vercel Dashboard.
   - Click **Add New Project**.
   - Import your GitHub repository.
3. **Configure the Project**:
   - **Framework Preset**: Vercel should automatically detect `Vite`.
   - **Root Directory**: Click "Edit" and select the `frontend` folder (since the React app is located in `frontend/`).
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
4. **Deploy**:
   - Click **Deploy**. Vercel will install dependencies, build the Vite app, and assign it a public `.vercel.app` URL.

---

## 4. Verification

1. **Test the UI**: Open the Vercel URL in your browser.
2. **Test the Connection**: Ask one of the example questions (e.g., "What is the expense ratio of HDFC Small Cap?").
3. **Verify the Response**: Ensure the bot replies within 3 sentences, includes the Groww citation, and displays the "Last updated from sources" footer.
