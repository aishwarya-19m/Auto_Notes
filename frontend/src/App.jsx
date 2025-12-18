import React, { useState, useEffect } from 'react'
import axios from 'axios'
import Header from './components/Header'
import InputSection from './components/InputSection'
import NotesDisplay from './components/NotesDisplay'
import LoadingSpinner from './components/LoadingSpinner'
import ErrorMessage from './components/ErrorMessage'
import HowItWorks from './components/HowItWorks'
import Features from './components/Features'
import AuthModal from './components/AuthModal'
import Background from './components/Background'

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

function App() {
  const [darkMode, setDarkMode] = useState(() => {
    const saved = localStorage.getItem('darkMode')
    return saved ? JSON.parse(saved) : true // Default to dark mode for "premium" feel
  })
  const [notes, setNotes] = useState(null)
  const [transcript, setTranscript] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [isAuthOpen, setIsAuthOpen] = useState(false)

  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add('dark')
    } else {
      document.documentElement.classList.remove('dark')
    }
    localStorage.setItem('darkMode', JSON.stringify(darkMode))
  }, [darkMode])

  // Check backend health on mount
  useEffect(() => {
    const checkBackend = async () => {
      try {
        await axios.get(`${API_BASE_URL}/`)
      } catch (err) {
        console.error('Backend check failed:', err)
        setError('Cannot connect to backend server. Please ensure the backend is running on port 8000.')
      }
    }
    checkBackend()
  }, [])

  const handleGenerateNotes = async (source, data) => {
    setLoading(true)
    setError(null)
    setNotes(null)
    setTranscript(null)

    try {
      let response

      if (source === 'youtube') {
        response = await axios.post(`${API_BASE_URL}/api/generate-notes/youtube`, {
          url: data
        })
      } else if (source === 'upload') {
        const formData = new FormData()
        formData.append('file', data)
        response = await axios.post(`${API_BASE_URL}/api/generate-notes/upload`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
      }

      if (response.data.success) {
        setNotes(response.data.notes)
        setTranscript(response.data.transcript)
      }
    } catch (err) {
      const errorMessage = err.response?.data?.detail || err.message || 'An error occurred while generating notes'
      setError(errorMessage)
    } finally {
      setLoading(false)
    }
  }

  const handleExport = async (format) => {
    if (!notes || !transcript) {
      setError('No notes available to export')
      return
    }

    try {
      const response = await axios.post(
        `${API_BASE_URL}/api/export/${format}`,
        {
          transcript: transcript,
          notes: notes
        },
        {
          responseType: 'blob'
        }
      )

      const url = window.URL.createObjectURL(new Blob([response.data]))
      const link = document.createElement('a')
      link.href = url
      link.setAttribute('download', `notes.${format}`)
      document.body.appendChild(link)
      link.click()
      link.remove()
      window.URL.revokeObjectURL(url)
    } catch (err) {
      const errorMessage = err.response?.data?.detail || err.message || 'Error exporting notes'
      setError(errorMessage)
    }
  }

  const handleClear = () => {
    setNotes(null)
    setTranscript(null)
    setError(null)
  }

  return (
    <div className="min-h-screen transition-colors duration-300 font-sans selection:bg-primary-500/30 selection:text-primary-900 dark:selection:text-white pb-20">
      <Background />

      <Header
        darkMode={darkMode}
        setDarkMode={setDarkMode}
        onOpenAuth={() => setIsAuthOpen(true)}
      />

      <main className="relative z-10 container mx-auto px-4 pt-28 max-w-6xl">
        {/* Intro Section */}
        {!notes && !loading && (
          <div className="text-center mb-16 animate-fade-in">
            <h1 className="text-5xl md:text-6xl font-display font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-gray-900 to-gray-600 dark:from-white dark:to-gray-400 mb-6 tracking-tight">
              Transform Content into <br />
              <span className="text-gradient">Intelligent Notes</span>
            </h1>
            <p className="text-xl text-gray-600 dark:text-gray-400 max-w-2xl mx-auto leading-relaxed">
              Instantly generate structured summaries, key takeaways, and action items from YouTube videos and audio files.
            </p>
          </div>
        )}

        {/* Input Area */}
        {!notes && (
          <InputSection
            onGenerate={handleGenerateNotes}
            loading={loading}
          />
        )}

        {/* Landing Page Content (only show when no notes are generated) */}
        {!notes && !loading && (
          <>
            <HowItWorks />
            <Features />
          </>
        )}

        {/* Loading State */}
        {loading && <LoadingSpinner />}

        {/* Results Area */}
        {notes && (
          <NotesDisplay
            notes={notes}
            transcript={transcript}
            onExport={handleExport}
            onClear={handleClear}
          />
        )}
      </main>

      {/* Global Components */}
      <ErrorMessage
        message={error}
        onDismiss={() => setError(null)}
      />

      <AuthModal
        isOpen={isAuthOpen}
        onClose={() => setIsAuthOpen(false)}
      />
    </div>
  )
}

export default App
