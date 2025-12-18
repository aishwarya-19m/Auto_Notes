import os
import google.generativeai as genai
from typing import Optional

# Graceful handling for Whisper/Torch DLL errors (keeping imports for fallback if ever needed, but priority is Google)
WHISPER_AVAILABLE = False
try:
    import whisper
    WHISPER_AVAILABLE = True
except (OSError, ImportError, Exception):
    WHISPER_AVAILABLE = False

class TranscriptionService:
    def __init__(self):
        self.model_size = os.getenv("WHISPER_MODEL_SIZE", "base")
        self.model = None
        self.api_key = os.getenv("GOOGLE_API_KEY")
        
        if self.api_key:
            genai.configure(api_key=self.api_key)
            print("Google Gemini API initialized for transcription.")
        else:
            print("WARNING: GOOGLE_API_KEY not found. Transcription might fail.")

        # Local whisper loading (optional fallback, likely invalid on this machine)
        global WHISPER_AVAILABLE
        if WHISPER_AVAILABLE:
            try:
                # self.model = whisper.load_model(self.model_size) # Skip loading local model to save memory/startup time if we have API
                pass
            except Exception:
                pass

    async def transcribe_audio(self, file_path: str) -> Optional[str]:
        """
        Transcribe audio file using Google Gemini Flash (multimodal).
        """
        if not self.api_key:
             return "SYSTEM MESSAGE: Real transcription unavailable. Missing GOOGLE_API_KEY."

        try:
            print("Uploading audio to Gemini...")
            # Upload the file to Gemini
            audio_file = genai.upload_file(path=file_path)
            print(f"Uploaded file: {audio_file.uri}")
            
            # Generate content using Gemini 1.5 Flash (efficient for audio)
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = "Please transcribe the spoken content of this audio file accurate verbatim. Do not add any commentary."
            response = model.generate_content([prompt, audio_file])
            
            print("Gemini transcription successful.")
            return response.text
            
        except Exception as e:
            print(f"Gemini transcription failed: {str(e)}")
            return f"Error during transcription: {str(e)}"


