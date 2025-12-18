# AutoNotes Pro

A modern web application that generates structured notes from YouTube videos and audio files using AI. Built with FastAPI (Python) and React.

## Features

### Frontend
- ✅ Input field for YouTube video links
- ✅ Upload option for recorded lecture files (MP3, MP4, WAV, M4A, WEBM)
- ✅ "Generate Notes" button to trigger backend processing
- ✅ Display notes in a structured format (headings, bullet points, summaries)
- ✅ Responsive design for desktop and mobile
- ✅ Dark mode toggle
- ✅ Export notes as PDF or TXT

### Backend
- ✅ FastAPI REST API
- ✅ Extract transcript from YouTube videos using `youtube-transcript-api`
- ✅ Transcribe uploaded audio files using OpenAI's Whisper
- ✅ Summarize transcripts into systematic notes using OpenAI API
- ✅ Organize notes into sections: Introduction, Key Points, Examples, Conclusion
- ✅ Export options (PDF, TXT)

## Tech Stack

- **Backend**: Python, FastAPI, Uvicorn
- **Frontend**: React, Vite, TailwindCSS
- **Libraries**: 
  - `youtube-transcript-api` - YouTube transcript extraction
  - `openai-whisper` - Audio transcription
  - `openai` - AI-powered note generation
  - `reportlab` - PDF export
  - `python-dotenv` - Environment variable management

## Prerequisites

- Python 3.8 or higher
- Node.js 16 or higher
- FFmpeg (required for Whisper audio processing)
  - **Windows**: Download from [FFmpeg website](https://ffmpeg.org/download.html) and add to PATH
  - **macOS**: `brew install ffmpeg`
  - **Linux**: `sudo apt-get install ffmpeg` or `sudo yum install ffmpeg`
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd "Autonotes Pro"
```

### 2. Backend Setup

```bash
cd backend

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Edit .env and add your OpenAI API key
# OPENAI_API_KEY=your_api_key_here
```

### 3. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install
```

## Running the Application

### Start the Backend

```bash
cd backend

# Activate virtual environment if not already activated
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Run the server
python main.py
# Or use uvicorn directly:
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The backend will be available at `http://localhost:8000`

### Start the Frontend

```bash
cd frontend

# Run the development server
npm run dev
```

The frontend will be available at `http://localhost:3000`

## Usage

1. **For YouTube Videos:**
   - Navigate to the "YouTube Video" tab
   - Paste a YouTube video URL
   - Click "Generate Notes"
   - Wait for processing (transcript extraction + AI summarization)

2. **For Audio/Video Files:**
   - Navigate to the "Upload File" tab
   - Click "Upload a file" or drag and drop
   - Select an audio/video file (MP3, MP4, WAV, M4A, WEBM)
   - Click "Generate Notes"
   - Wait for processing (transcription + AI summarization)

3. **Export Notes:**
   - After notes are generated, click "Export PDF" or "Export TXT"
   - The file will be downloaded automatically

## Project Structure

```
Autonotes Pro/
├── backend/
│   ├── main.py                 # FastAPI application entry point
│   ├── services/
│   │   ├── youtube_service.py      # YouTube transcript extraction
│   │   ├── transcription_service.py # Whisper audio transcription
│   │   ├── summarization_service.py # OpenAI note generation
│   │   └── export_service.py       # PDF/TXT export
│   ├── requirements.txt        # Python dependencies
│   ├── .env.example            # Environment variables template
│   ├── uploads/                 # Temporary upload directory
│   └── exports/                 # Generated export files
├── frontend/
│   ├── src/
│   │   ├── App.jsx              # Main React component
│   │   ├── components/
│   │   │   ├── Header.jsx           # Header with dark mode toggle
│   │   │   ├── InputSection.jsx     # YouTube/Upload input
│   │   │   ├── NotesDisplay.jsx     # Notes display and export
│   │   │   ├── LoadingSpinner.jsx   # Loading indicator
│   │   │   └── ErrorMessage.jsx     # Error display
│   │   ├── main.jsx             # React entry point
│   │   └── index.css            # Global styles
│   ├── package.json             # Node.js dependencies
│   ├── vite.config.js           # Vite configuration
│   └── tailwind.config.js       # TailwindCSS configuration
└── README.md                    # This file
```

## API Endpoints

### POST `/api/generate-notes/youtube`
Generate notes from a YouTube video URL.

**Request Body:**
```json
{
  "url": "https://www.youtube.com/watch?v=..."
}
```

**Response:**
```json
{
  "success": true,
  "transcript": "...",
  "notes": {
    "formatted": "...",
    "structured": {...}
  }
}
```

### POST `/api/generate-notes/upload`
Generate notes from an uploaded audio/video file.

**Request:** Multipart form data with `file` field

**Response:**
```json
{
  "success": true,
  "transcript": "...",
  "notes": {
    "formatted": "...",
    "structured": {...}
  }
}
```

### POST `/api/export/pdf`
Export notes as PDF.

**Request Body:**
```json
{
  "transcript": "...",
  "notes": {...}
}
```

**Response:** PDF file download

### POST `/api/export/txt`
Export notes as TXT.

**Request Body:**
```json
{
  "transcript": "...",
  "notes": {...}
}
```

**Response:** TXT file download

## Error Handling

The application includes comprehensive error handling for:
- Invalid YouTube URLs
- Videos without captions
- Unsupported file types
- Transcription failures
- API authentication errors
- Network errors

All errors are displayed to the user with clear, actionable messages.

## Configuration

### Environment Variables

Create a `.env` file in the `backend` directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
WHISPER_MODEL_SIZE=base  # Optional: tiny, base, small, medium, large
```

### Whisper Model Sizes

- `tiny`: Fastest, least accurate
- `base`: Good balance (default)
- `small`: Better accuracy
- `medium`: High accuracy
- `large`: Best accuracy, slowest

## Troubleshooting

### YouTube transcript extraction fails
- Ensure the video has captions available
- Check that the URL is valid and accessible
- Some videos may have disabled captions

### Audio transcription fails
- Ensure FFmpeg is installed and in PATH
- Check that the audio file is not corrupted
- Verify the file format is supported

### OpenAI API errors
- Verify your API key is correct in `.env`
- Check your OpenAI account has sufficient credits
- Ensure you have API access enabled

### Frontend can't connect to backend
- Ensure backend is running on port 8000
- Check CORS settings in `backend/main.py`
- Verify the API URL in frontend environment variables

## Future Enhancements

Potential features to add:
- User authentication (Google login)
- Save notes history per user
- Database integration for note storage
- Multiple language support
- Custom note templates
- Collaborative note sharing

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues and questions, please open an issue on the repository.



