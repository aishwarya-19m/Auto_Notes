"""
Service for extracting transcripts from YouTube videos.
"""
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
import re
from typing import Optional
import os
import time
import random
import time
import random


class YouTubeService:
    """
    Handles YouTube video transcript extraction.
    """
    
    def __init__(self):
        self.transcript_api = YouTubeTranscriptApi
    
    def _extract_video_id(self, url: str) -> str:
        """
        Extract video ID from various YouTube URL formats.
        
        Supported formats:
        - https://www.youtube.com/watch?v=VIDEO_ID
        - https://youtu.be/VIDEO_ID
        - https://www.youtube.com/embed/VIDEO_ID
        """
        # Parse URL
        parsed = urlparse(url)
        
        # Check for youtu.be short URLs
        if 'youtu.be' in parsed.netloc:
            video_id = parsed.path.lstrip('/')
            return video_id.split('?')[0]
        
        # Check for standard YouTube URLs
        if 'youtube.com' in parsed.netloc:
            query_params = parse_qs(parsed.query)
            if 'v' in query_params:
                return query_params['v'][0]
            
            # Check for embed URLs
            if '/embed/' in parsed.path:
                return parsed.path.split('/embed/')[1].split('?')[0]
        
        # Try to extract from any YouTube-like URL
        match = re.search(r'(?:v=|/)([0-9A-Za-z_-]{11}).*', url)
        if match:
            return match.group(1)
        
        raise ValueError("Invalid YouTube URL. Could not extract video ID.")
    
    async def get_transcript(self, url: str) -> str:
        """
        Extract transcript from YouTube video URL.
        
        Args:
            url: YouTube video URL
            
        Returns:
            Transcript text as a string
            
        Raises:
            ValueError: If video ID cannot be extracted or transcript is unavailable
        """
        try:
            # Extract video ID
            video_id = self._extract_video_id(url)
            
            # Try to get transcript with smart language handling and retry logic for rate limits
            transcript_list = None
            max_retries = 3
            base_delay = 2  # Base delay in seconds
            
            for attempt in range(max_retries):
                try:
                    # Add delay before retry (exponential backoff)
                    if attempt > 0:
                        delay = base_delay * (2 ** (attempt - 1)) + random.uniform(0, 1)
                        print(f"Rate limit detected. Waiting {delay:.1f} seconds before retry {attempt + 1}/{max_retries}...")
                        time.sleep(delay)
                    
                    # First, try to get English transcript directly
                    transcript_list = self.transcript_api.get_transcript(video_id, languages=['en'])
                    break  # Success, exit retry loop
                    
                except Exception as en_error:
                    error_msg = str(en_error)
                    
                    # Check if it's a rate limit error (429)
                    if "429" in error_msg or "Too Many Requests" in error_msg:
                        if attempt < max_retries - 1:
                            continue  # Will retry in next iteration
                        else:
                            # All retries exhausted
                            raise ValueError(
                                "YouTube rate limit exceeded after multiple attempts. "
                                "Please wait 5-10 minutes and try again, or try a different video. "
                                "You can also upload an audio file instead."
                            )
                    
                    # If not a rate limit error on first attempt, try translation approach
                    if attempt == 0:
                        try:
                            # If English not available, get any transcript and translate to English
                            # Get list of available transcripts
                            transcript_list_obj = self.transcript_api.list_transcripts(video_id)
                            
                            # Get any available transcript
                            transcript = None
                            
                            # Try different methods to get a transcript
                            # Method 1: Try to get any manual transcript
                            try:
                                for t in transcript_list_obj:
                                    if t.is_manually_created:
                                        transcript = t
                                        break
                            except:
                                pass
                            
                            # Method 2: If no manual, get any auto-generated transcript
                            if transcript is None:
                                try:
                                    for t in transcript_list_obj:
                                        if t.is_generated:
                                            transcript = t
                                            break
                                except:
                                    pass
                            
                            # Method 3: Last resort - get the first available transcript
                            if transcript is None:
                                try:
                                    transcript = next(iter(transcript_list_obj))
                                except:
                                    pass
                            
                            if transcript is None:
                                raise ValueError("No transcripts found for this video.")
                            
                            # Translate to English if not already English
                            if transcript.language_code != 'en':
                                try:
                                    transcript = transcript.translate('en')
                                except Exception as translate_err:
                                    # If translation fails, try to use original language
                                    print(f"Translation to English failed: {translate_err}. Using original language: {transcript.language_code}")
                                    # Continue with original language - better than nothing
                            
                            # Fetch the transcript data
                            transcript_list = transcript.fetch()
                            break  # Success, exit retry loop
                            
                        except Exception as translate_error:
                            error_msg = str(translate_error)
                            
                            # Check if it's a rate limit error
                            if "429" in error_msg or "Too Many Requests" in error_msg:
                                if attempt < max_retries - 1:
                                    continue  # Will retry
                                else:
                                    raise ValueError(
                                        "YouTube rate limit exceeded. Please wait a few minutes and try again, "
                                        "or try a different video. You can also upload an audio file instead."
                                    )
                            
                            # If not rate limit, raise error
                            if "No transcripts found" in error_msg:
                                raise ValueError(
                                    "No captions found for this video. Please ensure the video has closed captions (CC) enabled."
                                )
                            raise ValueError(
                                f"Could not retrieve or translate transcript to English: {error_msg[:200]}. "
                                f"Please try a different video with English captions or upload an audio file."
                            )
                    else:
                        # Subsequent attempts failed, re-raise the original error
                        raise ValueError(
                            f"Could not retrieve transcript after {max_retries} attempts: {error_msg[:200]}. "
                            f"Please try again later or upload an audio file."
                        )
            
            # Combine all transcript segments
            transcript_text = " ".join([item['text'] for item in transcript_list])
            
            return transcript_text
        
        except Exception as e:
            error_msg = str(e)
            # Re-raise nicely formatted errors
            if "No transcript found" in error_msg:
                 raise ValueError(
                    "No captions found for this video. Please ensure the video has closed captions (CC) enabled."
                )
            if "transcript" in error_msg.lower() or "caption" in error_msg.lower():
                raise ValueError(
                    f"Could not retrieve captions: {error_msg}. Please try a different video or upload an audio file."
                )
            raise ValueError(f"Error extracting transcript: {error_msg}")

    def download_audio(self, url: str, output_path: str) -> Optional[str]:
        """
        Download audio from YouTube video using yt-dlp.
        Returns the path to the downloaded file.
        """
        try:
            import yt_dlp
            
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': output_path + '.%(ext)s', # Let it append extension
                'quiet': True,
                'no_warnings': True
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            # Find the downloaded file
            # yt-dlp appends the extension to the output_path we gave it.
            # We look for any file in the directory that starts with our temp filename.
            directory = os.path.dirname(output_path)
            basename = os.path.basename(output_path)
            
            # Debug log
            print(f"Searching for file starting with '{basename}' in '{directory}'")

            files_in_dir = os.listdir(directory)
            for file in files_in_dir:
                if file.startswith(basename):
                    full_path = os.path.join(directory, file)
                    print(f"Found audio file: {full_path}")
                    return full_path
            
            print(f"No audio file found. Files in dir: {files_in_dir}")
            return None
            
        except Exception as e:
            print(f"Error downloading audio: {e}")
            return None

