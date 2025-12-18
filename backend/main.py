from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel, HttpUrl
from typing import Optional
import os
import tempfile
import shutil
import time
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from services.youtube_service import YouTubeService
from services.transcription_service import TranscriptionService
from services.summarization_service import SummarizationService
from services.export_service import ExportService

app = FastAPI(title="AutoNotes Pro API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001",
        "http://localhost:5173",
        "http://localhost:8000",
        "http://localhost:8001",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:3001",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:8000",
        "http://127.0.0.1:8001"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
youtube_service = YouTubeService()
transcription_service = TranscriptionService()
summarization_service = SummarizationService()
export_service = ExportService()

# Ensure uploads directory exists
UPLOADS_DIR = Path("uploads")
UPLOADS_DIR.mkdir(exist_ok=True)


class YouTubeRequest(BaseModel):
    url: str


class ExportRequest(BaseModel):
    transcript: str
    notes: dict


@app.get("/")
async def root():
    return {"message": "AutoNotes Pro API is running"}


@app.post("/api/generate-notes/youtube")
async def generate_notes_from_youtube(request: YouTubeRequest):
    """
    Extract transcript from YouTube video and generate notes.
    """
    try:
        # Extract transcript from YouTube
        transcript = await youtube_service.get_transcript(request.url)
        
        if not transcript:
            raise ValueError("Empty transcript returned")

        # Generate structured notes
        notes = await summarization_service.generate_notes(transcript)
        
        return JSONResponse(content={
            "success": True,
            "transcript": transcript,
            "notes": notes
        })
    
    except Exception as e:
        print(f"Caption retrieval failed: {str(e)}. Attempting audio download fallback...")
        
        # Fallback: Download audio and transcribe
        temp_audio = None
        try:
            timestamp = int(time.time())
            temp_dir = os.path.join(UPLOADS_DIR, "temp_dl")
            os.makedirs(temp_dir, exist_ok=True)
            
            # yt-dlp will append extension
            output_template = os.path.join(temp_dir, f"audio_{timestamp}")
            
            downloaded_file = youtube_service.download_audio(request.url, output_template)
            
            if not downloaded_file:
                 raise HTTPException(
                    status_code=400,
                    detail=f"Caption retrieval failed and audio download failed. Error: {str(e)}"
                )
            
            temp_audio = downloaded_file
            print(f"Audio downloaded to: {temp_audio}")
            
            # Transcribe
            transcript = await transcription_service.transcribe_audio(temp_audio)
            
            if not transcript:
                 raise HTTPException(
                    status_code=400,
                    detail="Could not transcribe downloaded audio."
                )
                
            # Generate structured notes
            notes = await summarization_service.generate_notes(transcript)
            
            return JSONResponse(content={
                "success": True,
                "transcript": transcript,
                "notes": notes
            })

        except Exception as fallback_error:
            # If fallback also fails, return original error or composite
            error_message = f"Failed to retrieve captions: {str(e)}. Fallback failed: {str(fallback_error)}"
            raise HTTPException(status_code=400, detail=error_message)
        
        finally:
            # Cleanup
            if temp_audio and os.path.exists(temp_audio):
                try:
                    os.unlink(temp_audio)
                except:
                    pass


@app.post("/api/generate-notes/upload")
async def generate_notes_from_upload(file: UploadFile = File(...)):
    """
    Transcribe uploaded audio/video file and generate notes.
    """
    # Validate file type
    allowed_extensions = {'.mp3', '.mp4', '.wav', '.m4a', '.webm'}
    file_ext = Path(file.filename).suffix.lower()
    
    if file_ext not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail=f"File type not supported. Allowed types: {', '.join(allowed_extensions)}"
        )
    
    # Save uploaded file temporarily
    temp_file = None
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=file_ext) as temp_file:
            shutil.copyfileobj(file.file, temp_file)
            temp_path = temp_file.name
        
        # Transcribe audio
        transcript = await transcription_service.transcribe_audio(temp_path)
        
        if not transcript:
            raise HTTPException(
                status_code=400,
                detail="Could not transcribe audio. Please ensure the file contains clear audio."
            )
        
        # Generate structured notes
        notes = await summarization_service.generate_notes(transcript)
        
        return JSONResponse(content={
            "success": True,
            "transcript": transcript,
            "notes": notes
        })
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")
    
    finally:
        # Clean up temporary file
        if temp_file and os.path.exists(temp_path):
            os.unlink(temp_path)


@app.post("/api/export/pdf")
async def export_pdf(request: ExportRequest):
    """
    Export notes as PDF.
    """
    try:
        pdf_path = await export_service.export_to_pdf(request.transcript, request.notes)
        return FileResponse(
            pdf_path,
            media_type="application/pdf",
            filename="notes.pdf"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating PDF: {str(e)}")


@app.post("/api/export/txt")
async def export_txt(request: ExportRequest):
    """
    Export notes as TXT.
    """
    try:
        txt_path = await export_service.export_to_txt(request.transcript, request.notes)
        return FileResponse(
            txt_path,
            media_type="text/plain",
            filename="notes.txt"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating TXT: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    import socket
    
    # Try port 8000, fallback to 8001 if busy
    port = 8000
    try:
        # Test if port is available
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('0.0.0.0', port))
        print(f"Starting server on port {port}...")
    except OSError:
        port = 8001
        print(f"Port 8000 busy, using port {port} instead...")
    
    uvicorn.run(app, host="0.0.0.0", port=port)

