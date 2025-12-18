# Quick Setup Guide

Follow these steps to get AutoNotes Pro running on your machine.

## Prerequisites Check

Before starting, ensure you have:
- ✅ Python 3.8+ installed
- ✅ Node.js 16+ installed
- ✅ FFmpeg installed (for audio transcription)
- ✅ OpenAI API key

## Step-by-Step Setup

### 1. Install FFmpeg

**Windows:**
1. Download from https://ffmpeg.org/download.html
2. Extract and add `bin` folder to your PATH
3. Verify: Open PowerShell and run `ffmpeg -version`

**macOS:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows PowerShell:
.\venv\Scripts\Activate.ps1
# Windows CMD:
venv\Scripts\activate.bat
# macOS/Linux:
source venv/bin/activate

# Install Python packages
pip install -r requirements.txt

# Create .env file
copy .env.example .env  # Windows
# OR
cp .env.example .env   # macOS/Linux

# Edit .env file and add your OpenAI API key
# OPENAI_API_KEY=sk-your-key-here
```

### 3. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install Node packages
npm install
```

### 4. Run the Application

**Terminal 1 - Backend:**
```bash
cd backend
# Activate venv if not already activated
python main.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

### 5. Access the Application

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## Testing

1. **Test YouTube:**
   - Go to http://localhost:3000
   - Paste a YouTube URL (e.g., https://www.youtube.com/watch?v=dQw4w9WgXcQ)
   - Click "Generate Notes"

2. **Test File Upload:**
   - Go to "Upload File" tab
   - Upload an MP3 or MP4 file
   - Click "Generate Notes"

## Troubleshooting

### "FFmpeg not found"
- Ensure FFmpeg is installed and in your PATH
- Restart your terminal after installing

### "OpenAI API key not found"
- Check that `.env` file exists in `backend/` directory
- Verify the key is correctly formatted: `OPENAI_API_KEY=sk-...`

### "Module not found" errors
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt` again

### Frontend can't connect to backend
- Ensure backend is running on port 8000
- Check that CORS is enabled in `backend/main.py`

### Port already in use
- Change port in `frontend/vite.config.js` (frontend)
- Change port in `backend/main.py` (backend)

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check API documentation at http://localhost:8000/docs
- Customize Whisper model size in `.env` if needed



