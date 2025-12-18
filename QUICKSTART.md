# Quick Start Guide - How to Run AutoNotes Pro

## Prerequisites

Before running, make sure you have:
1. **Python 3.8+** installed
2. **Node.js 16+** installed  
3. **FFmpeg** installed (for audio transcription)
4. **OpenAI API Key** ([Get one here](https://platform.openai.com/api-keys))

## Step 1: Install FFmpeg (if not already installed)

**Windows:**
1. Download from: https://www.gyan.dev/ffmpeg/builds/
2. Extract the zip file
3. Add the `bin` folder to your system PATH
4. Verify: Open PowerShell and run `ffmpeg -version`

## Step 2: Set Up Backend

Open a terminal/PowerShell window:

```powershell
# Navigate to backend folder
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1
# If you get an execution policy error, run this first:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Install Python packages
pip install -r requirements.txt

# Create .env file from example
copy .env.example .env

# Edit .env file and add your OpenAI API key
# Use any text editor to open .env and replace:
# OPENAI_API_KEY=your_openai_api_key_here
# with your actual API key like:
# OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxx
```

## Step 3: Set Up Frontend

Open a **new** terminal/PowerShell window:

```powershell
# Navigate to frontend folder
cd frontend

# Install Node.js packages
npm install
```

## Step 4: Run the Application

### Terminal 1 - Start Backend Server

```powershell
cd backend
.\venv\Scripts\Activate.ps1
python main.py
```

You should see:
```
INFO:     Started server process
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**Keep this terminal open!**

### Terminal 2 - Start Frontend Server

```powershell
cd frontend
npm run dev
```

You should see:
```
  VITE v5.x.x  ready in xxx ms

  ➜  Local:   http://localhost:3000/
```

## Step 5: Use the Application

1. Open your browser and go to: **http://localhost:3000**
2. You'll see the AutoNotes Pro interface
3. Try it out:
   - **YouTube Tab**: Paste a YouTube URL and click "Generate Notes"
   - **Upload Tab**: Upload an audio/video file and click "Generate Notes"

## Troubleshooting

### "python is not recognized"
- Make sure Python is installed and added to PATH
- Try using `py` instead of `python` on Windows

### "npm is not recognized"
- Make sure Node.js is installed
- Restart your terminal after installing Node.js

### "FFmpeg not found"
- Install FFmpeg and add it to your PATH
- Restart terminal after adding to PATH

### "OPENAI_API_KEY not found"
- Make sure `.env` file exists in `backend/` folder
- Check that the file contains: `OPENAI_API_KEY=sk-your-key-here`
- No quotes around the key value

### "Port 8000 already in use"
- Another application is using port 8000
- Stop that application or change the port in `backend/main.py`

### "Port 3000 already in use"
- Another application is using port 3000
- Stop that application or change the port in `frontend/vite.config.js`

### Backend errors about missing modules
```powershell
cd backend
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Frontend errors about missing packages
```powershell
cd frontend
npm install
```

## API Documentation

Once the backend is running, you can view the API documentation at:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Stopping the Application

- Press `Ctrl+C` in both terminal windows to stop the servers



