# AutoNotes Pro - Project Technical Summary

This document provides a comprehensive overview of the technologies, tools, and libraries utilized in the development of **AutoNotes Pro**.

## 1. Frontend Technologies (User Interface)

The frontend is built to be modern, responsive, and visually engaging, following a "Premium SaaS" aesthetic.

*   **Core Framework**:
    *   **React (v18)**: A JavaScript library for building user interfaces.
    *   **Vite**: A build tool that provides a faster development experience and optimized builds.

*   **Styling & Design**:
    *   **Tailwind CSS**: A utility-first CSS framework for rapid UI development.
    *   **PostCSS & Autoprefixer**: Tools for transforming CSS and ensuring cross-browser compatibility.
    *   **Glassmorphism**: Custom CSS implementation for translucent, frosted-glass effects on cards and headers.
    *   **Google Fonts**:
        *   **Outfit**: Used for headings (bold, modern feel).
        *   **Inter**: Used for body text (clean, high readability).

*   **Icons & Assets**:
    *   **Heroicons**: A set of free, SVG icons (React version) for UI elements like buttons, tabs, and feature lists.

*   **State Management & Logic**:
    *   **React Hooks**: `useState`, `useEffect` for managing component state and lifecycle.
    *   **Axios**: A promise-based HTTP client for making API requests to the backend.

## 2. Backend Technologies (Server & Logic)

The backend is a robust Python-based API that handles data processing, AI interactions, and file management.

*   **Core Framework**:
    *   **FastAPI**: A high-performance web framework for building APIs with Python.
    *   **Uvicorn**: An ASGI web server implementation to run the FastAPI application.

*   **AI & Machine Learning**:
    *   **OpenAI API (GPT-3.5 Turbo)**: Used for generating summaries, picking key points, and structuring the notes.
    *   **OpenAI Whisper**: A general-purpose speech recognition model used for local audio transcription.
    *   **PyTorch (CPU Version)**: The underlying machine learning library required to run Whisper locally.

*   **Data Processing & Utilities**:
    *   **YouTube Transcript API**: A library to extract transcripts/captions directly from YouTube videos.
    *   **yt-dlp**: A command-line program to download videos/audio from YouTube (used as a fallback when captions are missing).
    *   **ReportLab**: A library for generating PDF documents programmatically.
    *   **Pydantic**: Data validation and settings management using Python type annotations.
    *   **Python-Multipart**: Required for parsing form data (file uploads).
    *   **Python-Dotenv**: Loads environment variables from a `.env` file (for secure API key storage).

## 3. Key Features & Implementations

*   **Robust Fallback System**:
    *   If YouTube captions are unavailable, the system automatically downloads the audio using `yt-dlp` and transcribes it locally.
    *   If the OpenAI API key is missing/invalid ("Simulation Mode"), the system uses the *actual* transcript text to generate "Offline Notes" instead of mock data.
*   **Dual-Theming**: Complete Dark Mode and Light Mode support with smooth CSS transitions.
*   **Export Capabilities**: Notes can be exported as structured **PDFs** or **Text files**.

## 4. Development Environment

*   **Node.js**: Runtime environment for the frontend tooling.
*   **Python (3.13)**: Runtime environment for the backend logic.
*   **Git**: Version control (implied).
*   **Visual Studio Code**: Recommended IDE.
*   **Windows OS**: The hosting operating system.
