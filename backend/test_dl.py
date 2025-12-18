import yt_dlp
import os

def download_audio(url, output_path):
    print(f"Testing download for: {url}")
    print(f"Output to: {output_path}")
    
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_path + '.%(ext)s', 
            'quiet': False, # Show output for debugging
            'no_warnings': False
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        # Check files
        directory = os.path.dirname(output_path)
        basename = os.path.basename(output_path)
        
        print("\nChecking directory contents:")
        found = False
        for file in os.listdir(directory):
            print(f"- {file}")
            if file.startswith(basename):
                found = True
        
        if found:
            print("\nSUCCESS: File downloaded.")
        else:
            print("\nFAILURE: File not found after download.")

    except Exception as e:
        print(f"\nCRITICAL ERROR: {e}")

if __name__ == "__main__":
    # Test with "Me at the zoo" - short, static video
    download_audio("https://www.youtube.com/watch?v=jNQXAC9IVRw", "test_audio_download")
