# How to Run AutoNotes Pro

## Quick Start Guide

### Step 1: Make sure dependencies are installed

If you haven't already, install all Python packages:

```powershell
cd "C:\Users\Aishwarya\Desktop\Autonotes Pro\backend"
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Step 2: Set up your OpenAI API key

1. Make sure you have a `.env` file in the `backend` folder
2. If it doesn't exist, copy the example:
   ```powershell
   copy .env.example .env
   ```
3. Edit `.env` file and add your OpenAI API key:
   ```
   OPENAI_API_KEY=sk-your-actual-api-key-here
   ```

### Step 3: Run the Backend Server

**Open Terminal/PowerShell Window 1:**

```powershell
cd "C:\Users\Aishwarya\Desktop\Autonotes Pro\backend"
.\venv\Scripts\Activate.ps1
python main.py
```

You should see:
```
INFO:     Started server process
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

**Keep this terminal window open!**

### Step 4: Run the Frontend Server

**Open a NEW Terminal/PowerShell Window 2:**

```powershell
cd "C:\Users\Aishwarya\Desktop\Autonotes Pro\frontend"
npm install
npm run dev
```

You should see:
```
  VITE v5.x.x  ready in xxx ms

  ➜  Local:   http://localhost:3000/
```

### Step 5: Open in Browser

Open your web browser and go to:
**http://localhost:3000**

## Using the Application

1. **For YouTube Videos:**
   - Click on "YouTube Video" tab
   - Paste a YouTube URL (e.g., `https://www.youtube.com/watch?v=dQw4w9WgXcQ`)
   - Click "Generate Notes"
   - Wait for processing

2. **For Audio/Video Files:**
   - Click on "Upload File" tab
   - Click "Upload a file" or drag and drop
   - Select an MP3, MP4, WAV, M4A, or WEBM file
   - Click "Generate Notes"
   - Wait for processing

3. **Export Notes:**
   - After notes are generated, click "Export PDF" or "Export TXT"
   - File will download automatically

## Stopping the Application

- Press `Ctrl+C` in both terminal windows to stop the servers

## Troubleshooting

### Backend won't start
- Make sure virtual environment is activated (you should see `(venv)` in prompt)
- Check that `.env` file exists and has your OpenAI API key
- Verify all packages are installed: `pip list`

### Frontend won't start
- Make sure you ran `npm install` first
- Check that Node.js is installed: `node --version`

### "OPENAI_API_KEY not found" error
- Check `.env` file exists in `backend/` folder
- Verify the key is formatted correctly: `OPENAI_API_KEY=sk-...` (no quotes)

### Port already in use
- Stop other applications using ports 3000 or 8000
- Or change ports in configuration files


