import os
import google.generativeai as genai
from typing import Dict, Any


class SummarizationService:
    """
    Handles AI-powered note generation from transcripts using Google Gemini.
    """
    
    def __init__(self):
        """
        Initialize Google Gemini client.
        """
        self.api_key = os.getenv("GOOGLE_API_KEY")
        self.mock_mode = False
        
        if not self.api_key:
            print("WARNING: GOOGLE_API_KEY not found. Summarization will be in SIMULATION MODE.")
            self.mock_mode = True
        else:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-1.5-flash')
            

    async def generate_notes(self, transcript: str) -> Dict[str, Any]:
        """
        Generate structured notes from transcript.
        """
        # Return mock data if in simulation mode
        if self.mock_mode:
            return self._get_mock_notes(transcript)

        try:
            # Gemini has a large context window, so we are less worried about truncation, 
            # but still good practice to check if extremely large. 
            # 1.5 Flash has 1M context, so effectively no limit for this use case.
            
            prompt = f"""Analyze the following transcript and create well-structured notes. 
Organize the content into clear sections with headings, bullet points, and summaries.

Transcript:
{transcript}

Please create structured notes with the following format:
1. Introduction - A brief overview of the topic
2. Key Points - Main concepts and important information (use bullet points)
3. Examples - Specific examples or case studies mentioned (use bullet points)
4. Conclusion - Summary of main takeaways

Format the response as clear, readable notes that would be useful for studying or reference.
Use markdown formatting with headings (##), bullet points (-), and emphasis where appropriate."""

            response = self.model.generate_content(prompt)
            notes_text = response.text
            
            # Parse the notes into structured format
            structured_notes = self._parse_notes(notes_text)
            
            return {
                "formatted": notes_text,
                "structured": structured_notes
            }
        
        except Exception as e:
            error_msg = str(e)
            print(f"Error generating notes: {error_msg}")
            
            # Fallback to mock mode on critical errors
            if "key" in error_msg.lower() or "permission" in error_msg.lower():
                print("Authentication error detected. Falling back to SIMULATION MODE.")
                return self._get_mock_notes(transcript)
            
            # Return partial error info if just generation failed
            return {
                "formatted": f"Error generating notes with AI: {error_msg}",
                "structured": self._get_mock_notes(transcript)["structured"]
            }
    def _get_mock_notes(self, transcript_text: str = ""):
        """Returns structured data using the actual transcript (Offline Mode)."""
        
        # Create a basic summary from the input text
        # Take first 500 chars for intro
        intro = transcript_text[:500] + "..." if len(transcript_text) > 500 else transcript_text
        if not intro:
            intro = "No content available to summarize."
            
        conclusion = "Note: This content is generated in Offline Mode. For advanced AI summarization, please configure a valid Google Gemini API Key."
        
        # Extract pseudo-keypoints (just split sentences)
        sentences = [s.strip() for s in transcript_text.replace('\n', ' ').split('.') if len(s) > 20]
        key_points = sentences[:5] if sentences else ["No key points detected."]
        
        return {
            "formatted": f"# Offline Notes\n\n## Transcript Preview\n{intro}\n\n## Key Excerpts\n" + "\n".join([f"- {kp}" for kp in key_points]) + f"\n\n## System Message\n{conclusion}",
            "structured": {
                "introduction": intro,
                "key_points": key_points,
                "examples": ["Available in full transcript."],
                "conclusion": conclusion,
                "summary": f"{intro}\n\n{conclusion}"
            }
        }
    
    def _parse_notes(self, notes_text: str) -> Dict[str, Any]:
        """
        Parse markdown-formatted notes into structured dictionary.
        
        Args:
            notes_text: Markdown-formatted notes
            
        Returns:
            Structured dictionary with sections
        """
        lines = notes_text.split('\n')
        
        structured = {
            "introduction": "",
            "key_points": [],
            "examples": [],
            "conclusion": "",
            "summary": ""
        }
        
        current_section = None
        current_content = []
        
        for line in lines:
            line = line.strip()
            
            # Detect section headers
            if line.startswith('##'):
                # Save previous section
                if current_section and current_content:
                    content = '\n'.join(current_content).strip()
                    if current_section == "introduction":
                        structured["introduction"] = content
                    elif current_section == "conclusion":
                        structured["conclusion"] = content
                
                # Start new section
                header_lower = line.lower()
                if "introduction" in header_lower or "overview" in header_lower:
                    current_section = "introduction"
                elif "key point" in header_lower or "main" in header_lower:
                    current_section = "key_points"
                elif "example" in header_lower:
                    current_section = "examples"
                elif "conclusion" in header_lower or "summary" in header_lower:
                    current_section = "conclusion"
                else:
                    current_section = None
                
                current_content = []
            
            # Collect content
            elif line and current_section:
                if line.startswith('-') or line.startswith('*'):
                    # Bullet point
                    point = line.lstrip('-* ').strip()
                    if current_section == "key_points":
                        structured["key_points"].append(point)
                    elif current_section == "examples":
                        structured["examples"].append(point)
                else:
                    current_content.append(line)
        
        # Save last section
        if current_section and current_content:
            content = '\n'.join(current_content).strip()
            if current_section == "introduction":
                structured["introduction"] = content
            elif current_section == "conclusion":
                structured["conclusion"] = content
        
        # Create summary from introduction and conclusion
        if structured["introduction"] or structured["conclusion"]:
            structured["summary"] = f"{structured['introduction']}\n\n{structured['conclusion']}".strip()
        
        return structured



