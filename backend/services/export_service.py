"""
Service for exporting notes to PDF and TXT formats.
"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from datetime import datetime
import os
import tempfile
from pathlib import Path


class ExportService:
    """
    Handles export of notes to various formats.
    """
    
    def __init__(self):
        self.export_dir = Path("exports")
        self.export_dir.mkdir(exist_ok=True)
    
    async def export_to_pdf(self, transcript: str, notes: dict) -> str:
        """
        Export notes to PDF format.
        
        Args:
            transcript: Original transcript text
            notes: Notes dictionary (from summarization service)
            
        Returns:
            Path to generated PDF file
        """
        try:
            # Create temporary PDF file
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            pdf_path = self.export_dir / f"notes_{timestamp}.pdf"
            
            # Create PDF document
            doc = SimpleDocTemplate(str(pdf_path), pagesize=letter)
            story = []
            
            # Define styles
            styles = getSampleStyleSheet()
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=24,
                textColor='#1a1a1a',
                spaceAfter=30,
                alignment=TA_CENTER
            )
            heading_style = ParagraphStyle(
                'CustomHeading',
                parent=styles['Heading2'],
                fontSize=16,
                textColor='#2c3e50',
                spaceAfter=12,
                spaceBefore=20
            )
            normal_style = ParagraphStyle(
                'CustomNormal',
                parent=styles['Normal'],
                fontSize=11,
                textColor='#333333',
                spaceAfter=12,
                leading=14
            )
            
            # Title
            story.append(Paragraph("AutoNotes Pro - Generated Notes", title_style))
            story.append(Spacer(1, 0.2*inch))
            story.append(Paragraph(f"Generated on: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}", normal_style))
            story.append(Spacer(1, 0.3*inch))
            
            # Notes content
            notes_text = notes.get("formatted", "")
            if notes_text:
                # Split by sections and format
                lines = notes_text.split('\n')
                for line in lines:
                    line = line.strip()
                    if not line:
                        story.append(Spacer(1, 0.1*inch))
                    elif line.startswith('##'):
                        # Heading
                        heading_text = line.lstrip('#').strip()
                        story.append(Paragraph(heading_text, heading_style))
                    elif line.startswith('#'):
                        # Subheading
                        heading_text = line.lstrip('#').strip()
                        story.append(Paragraph(heading_text, heading_style))
                    else:
                        # Regular text
                        story.append(Paragraph(line, normal_style))
            
            # Add transcript section
            story.append(PageBreak())
            story.append(Paragraph("Full Transcript", heading_style))
            story.append(Spacer(1, 0.2*inch))
            
            # Truncate transcript if too long for PDF
            transcript_preview = transcript[:5000] + "..." if len(transcript) > 5000 else transcript
            story.append(Paragraph(transcript_preview.replace('\n', '<br/>'), normal_style))
            
            # Build PDF
            doc.build(story)
            
            return str(pdf_path)
        
        except Exception as e:
            raise ValueError(f"Error generating PDF: {str(e)}")
    
    async def export_to_txt(self, transcript: str, notes: dict) -> str:
        """
        Export notes to TXT format.
        
        Args:
            transcript: Original transcript text
            notes: Notes dictionary (from summarization service)
            
        Returns:
            Path to generated TXT file
        """
        try:
            # Create temporary TXT file
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            txt_path = self.export_dir / f"notes_{timestamp}.txt"
            
            # Write content to file
            with open(txt_path, 'w', encoding='utf-8') as f:
                f.write("=" * 60 + "\n")
                f.write("AutoNotes Pro - Generated Notes\n")
                f.write("=" * 60 + "\n\n")
                f.write(f"Generated on: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}\n\n")
                f.write("-" * 60 + "\n\n")
                
                # Write notes
                notes_text = notes.get("formatted", "")
                if notes_text:
                    f.write(notes_text)
                    f.write("\n\n")
                
                f.write("-" * 60 + "\n\n")
                f.write("Full Transcript\n")
                f.write("-" * 60 + "\n\n")
                f.write(transcript)
            
            return str(txt_path)
        
        except Exception as e:
            raise ValueError(f"Error generating TXT: {str(e)}")

