# How to Run AutoNotes Pro - Complete Guide

## Prerequisites Check

Before starting, make sure you have:
- ✅ Python 3.8+ installed
- ✅ Node.js 16+ installed
- ✅ OpenAI API key (in `backend/.env` file)
- ✅ FFmpeg installed (for audio transcription)

---

## Step-by-Step Instructions

### STEP 1: Start the Backend Server

**Open Terminal/PowerShell Window 1:**

```powershell
# Navigate to backend folder
cd "C:\Users\Aishwarya\Desktop\Autonotes Pro\backend"

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Start the backend server
python main.py
```

**You should see:**
```
INFO:     Started server process
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

**✅ Keep this terminal window open!**

**Alternative: Use the startup script:**
```powershell
cd "C:\Users\Aishwarya\Desktop\Autonotes Pro\backend"
.\start_backend.ps1
```

---

### STEP 2: Start the Frontend Server

**Open a NEW Terminal/PowerShell Window 2:**

```powershell
# Navigate to frontend folder
cd "C:\Users\Aishwarya\Desktop\Autonotes Pro\frontend"

# Install dependencies (only needed first time)
npm install

# Start the frontend development server
npm run dev
```

**You should see:**
```
  VITE v5.x.x  ready in xxx ms

  ➜  Local:   http://localhost:3000/
```

**✅ Keep this terminal window open too!**

---

### STEP 3: Open the Application

1. Open your web browser
2. Go to: **http://localhost:3000**
3. You should see the AutoNotes Pro interface

---

## Quick Reference

### Backend Commands

**Start Backend:**
```powershell
cd backend
.\venv\Scripts\Activate.ps1
python main.py
```

**Stop Backend:**
- Press `Ctrl+C` in the backend terminal window

**Check if Backend is Running:**
- Open browser: http://localhost:8000
- Should see: `{"message":"AutoNotes Pro API is running"}`

---

### Frontend Commands

**Start Frontend:**
```powershell
cd frontend
npm run dev
```

**Stop Frontend:**
- Press `Ctrl+C` in the frontend terminal window

**Build for Production:**
```powershell
cd frontend
npm run build
```

---

## Troubleshooting

### Backend won't start?

1. **Check virtual environment is activated:**
   ```powershell
   # You should see (venv) in your prompt
   (venv) PS C:\Users\...\backend>
   ```

2. **Check dependencies are installed:**
   ```powershell
   pip list
   # Should show fastapi, uvicorn, openai, etc.
   ```

3. **Check .env file exists:**
   ```powershell
   # In backend folder
   dir .env
   # Should show the file exists
   ```

4. **Install missing dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

---

### Frontend won't start?

1. **Check Node.js is installed:**
   ```powershell
   node --version
   # Should show v16 or higher
   ```

2. **Install dependencies:**
   ```powershell
   cd frontend
   npm install
   ```

3. **Check if port 3000 is in use:**
   ```powershell
   # Stop other applications using port 3000
   # Or change port in vite.config.js
   ```

---

### "Network Error" in Browser?

1. **Verify backend is running:**
   - Open: http://localhost:8000
   - Should see API response

2. **Check both servers are running:**
   - Backend terminal should show "Uvicorn running"
   - Frontend terminal should show "Local: http://localhost:3000"

3. **Try hard refresh in browser:**
   - Press `Ctrl+Shift+R` or `Ctrl+F5`

4. **Check browser console:**
   - Press `F12` → Console tab
   - Look for error messages

---

### "OPENAI_API_KEY not found" Error?

1. **Check .env file exists:**
   ```powershell
   cd backend
   dir .env
   ```

2. **Create .env file if missing:**
   ```powershell
   copy .env.example .env
   ```

3. **Edit .env file and add your API key:**
   ```
   OPENAI_API_KEY=sk-your-actual-api-key-here
   ```

4. **Restart backend after adding key**

---

## Testing the Application

### Test YouTube Video:
1. Go to http://localhost:3000
2. Click "YouTube Video" tab
3. Paste a YouTube URL (e.g., `https://www.youtube.com/watch?v=dQw4w9WgXcQ`)
4. Click "Generate Notes"
5. Wait for processing

### Test File Upload:
1. Go to http://localhost:3000
2. Click "Upload File" tab
3. Click "Upload a file" or drag and drop
4. Select an MP3, MP4, WAV, M4A, or WEBM file
5. Click "Generate Notes"
6. Wait for processing

---

## Stopping the Application

**To stop both servers:**
1. Go to backend terminal → Press `Ctrl+C`
2. Go to frontend terminal → Press `Ctrl+C`

**Or simply close both terminal windows**

---

## Summary

**Two Terminal Windows Needed:**

**Terminal 1 (Backend):**
```powershell
cd backend
.\venv\Scripts\Activate.ps1
python main.py
```

**Terminal 2 (Frontend):**
```powershell
cd frontend
npm run dev
```

**Then open:** http://localhost:3000

---

## Need Help?

- Check API documentation: http://localhost:8000/docs
- Check backend status: http://localhost:8000
- Review error messages in terminal windows
- Check browser console (F12) for frontend errors

