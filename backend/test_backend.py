"""
Test script to verify backend is working correctly.
"""
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test that all modules can be imported."""
    print("Testing imports...")
    try:
        from services.youtube_service import YouTubeService
        from services.transcription_service import TranscriptionService
        from services.summarization_service import SummarizationService
        from services.export_service import ExportService
        from main import app
        print("✅ All imports successful!")
        return True
    except Exception as e:
        print(f"❌ Import error: {e}")
        return False

def test_services():
    """Test that services can be initialized."""
    print("\nTesting service initialization...")
    try:
        from services.youtube_service import YouTubeService
        from services.transcription_service import TranscriptionService
        from services.summarization_service import SummarizationService
        from services.export_service import ExportService
        
        youtube = YouTubeService()
        transcription = TranscriptionService()
        summarization = SummarizationService()
        export = ExportService()
        
        print("✅ All services initialized successfully!")
        return True
    except Exception as e:
        print(f"❌ Service initialization error: {e}")
        return False

def test_fastapi():
    """Test that FastAPI app can be created."""
    print("\nTesting FastAPI app...")
    try:
        from main import app
        print(f"✅ FastAPI app created: {app.title} v{app.version}")
        return True
    except Exception as e:
        print(f"❌ FastAPI error: {e}")
        return False

def test_env():
    """Test environment variables."""
    print("\nTesting environment variables...")
    from dotenv import load_dotenv
    load_dotenv()
    
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key and api_key != "your_openai_api_key_here":
        print("✅ OpenAI API key is set")
    else:
        print("⚠️  OpenAI API key not set (will use simulation mode)")
    
    return True

if __name__ == "__main__":
    print("=" * 50)
    print("Backend Test Suite")
    print("=" * 50)
    
    results = []
    results.append(("Imports", test_imports()))
    results.append(("Services", test_services()))
    results.append(("FastAPI", test_fastapi()))
    results.append(("Environment", test_env()))
    
    print("\n" + "=" * 50)
    print("Test Results:")
    print("=" * 50)
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{name}: {status}")
    
    all_passed = all(result for _, result in results)
    print("\n" + "=" * 50)
    if all_passed:
        print("✅ All tests passed! Backend is ready to run.")
        print("\nTo start the backend, run:")
        print("  python main.py")
    else:
        print("❌ Some tests failed. Please check the errors above.")
    print("=" * 50)

