# Vercel Deployment Guide

## Easy One-Click Setup

### Step 1: Push Your Code
Your code is already in GitHub: `https://github.com/abhineshkrsahu90/spd`

### Step 2: Deploy to Vercel
1. Go to [vercel.com](https://vercel.com)
2. Sign in with GitHub
3. Click "Add New" → "Project"
4. Import the repository: `abhineshkrsahu90/spd`
5. Click "Import"

### Step 3: Configuration
Vercel will auto-detect your project. No additional configuration needed!

The `vercel.json` file handles:
- ✅ Building the frontend from `frontend/` directory
- ✅ Running `npm install && npm run build`
- ✅ Serving static files from `frontend/dist`
- ✅ Routing all requests to `/index.html` (SPA support)

### Step 4: Environment Variables (Optional)
If you need to connect to a backend API:
1. Go to Project Settings → Environment Variables
2. Add: `VITE_API_BASE_URL = https://your-api-domain.com`

### Step 5: Deploy
Just click "Deploy" and Vercel will:
1. Clone your GitHub repo
2. Run the build command automatically
3. Deploy to production

That's it! 🎉

---

## Backend Deployment (Optional)

For backend (Flask), use:
- **Render.com** (free tier available)
- **Railway.app**
- **Heroku**

Or keep running locally on `localhost:5000` and update `VITE_API_BASE_URL` to point to your deployed backend.

## Testing Locally Before Deploying

```bash
# Frontend only
cd frontend
npm install
npm run build
npm run dev

# Backend (in separate terminal)
cd backend
python -m pip install -r requirements.txt
python run.py
```
