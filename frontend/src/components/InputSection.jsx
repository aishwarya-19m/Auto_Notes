import React, { useState } from 'react'
import { CloudArrowUpIcon, LinkIcon, SparklesIcon } from '@heroicons/react/24/outline'

function InputSection({ onGenerate, loading }) {
  const [activeTab, setActiveTab] = useState('youtube') // 'youtube' or 'upload'
  const [url, setUrl] = useState('')
  const [file, setFile] = useState(null)
  const [dragActive, setDragActive] = useState(false)

  const handleSubmit = (e) => {
    e.preventDefault()
    if (activeTab === 'youtube' && url) {
      onGenerate('youtube', url)
    } else if (activeTab === 'upload' && file) {
      onGenerate('upload', file)
    }
  }

  const handleDrag = (e) => {
    e.preventDefault()
    e.stopPropagation()
    if (e.type === 'dragenter' || e.type === 'dragover') {
      setDragActive(true)
    } else if (e.type === 'dragleave') {
      setDragActive(false)
    }
  }

  const handleDrop = (e) => {
    e.preventDefault()
    e.stopPropagation()
    setDragActive(false)
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      setFile(e.dataTransfer.files[0])
    }
  }

  return (
    <div className="w-full max-w-3xl mx-auto animate-fade-in">
      <div className="card p-1 sm:p-2 mb-8">
        {/* Tabs */}
        <div className="flex gap-1 p-1 bg-gray-50 dark:bg-slate-900/50 rounded-xl">
          <button
            onClick={() => setActiveTab('youtube')}
            className={`flex-1 flex items-center justify-center gap-2 py-3 rounded-lg text-sm font-medium transition-all duration-200 ${activeTab === 'youtube'
                ? 'bg-white dark:bg-slate-800 text-primary-600 dark:text-primary-400 shadow-sm'
                : 'text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-200'
              }`}
          >
            <LinkIcon className="w-5 h-5" />
            YouTube Link
          </button>
          <button
            onClick={() => setActiveTab('upload')}
            className={`flex-1 flex items-center justify-center gap-2 py-3 rounded-lg text-sm font-medium transition-all duration-200 ${activeTab === 'upload'
                ? 'bg-white dark:bg-slate-800 text-primary-600 dark:text-primary-400 shadow-sm'
                : 'text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-200'
              }`}
          >
            <CloudArrowUpIcon className="w-5 h-5" />
            Upload Audio
          </button>
        </div>

        {/* Content */}
        <div className="p-4 sm:p-6">
          <form onSubmit={handleSubmit} className="space-y-6">
            {activeTab === 'youtube' ? (
              <div className="animate-fade-in">
                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                  Paste YouTube URL
                </label>
                <div className="relative group">
                  <div className="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                    <LinkIcon className="h-5 w-5 text-gray-400 group-focus-within:text-primary-500 transition-colors" />
                  </div>
                  <input
                    type="url"
                    placeholder="https://www.youtube.com/watch?v=..."
                    value={url}
                    onChange={(e) => setUrl(e.target.value)}
                    className="input-field pl-11"
                    required
                  />
                </div>
                <p className="mt-2 text-xs text-gray-500 dark:text-gray-400">
                  Supports standard YouTube videos. Shorts support coming soon.
                </p>
              </div>
            ) : (
              <div className="animate-fade-in">
                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                  Upload Audio File
                </label>
                <div
                  className={`relative border-2 border-dashed rounded-xl p-8 transition-all duration-200 text-center cursor-pointer ${dragActive
                      ? 'border-primary-500 bg-primary-50 dark:bg-primary-900/10'
                      : 'border-gray-300 dark:border-slate-700 hover:border-primary-400 hover:bg-gray-50 dark:hover:bg-slate-800/50'
                    }`}
                  onDragEnter={handleDrag}
                  onDragLeave={handleDrag}
                  onDragOver={handleDrag}
                  onDrop={handleDrop}
                  onClick={() => document.getElementById('file-upload').click()}
                >
                  <input
                    id="file-upload"
                    type="file"
                    accept="audio/*,video/*"
                    className="hidden"
                    onChange={(e) => setFile(e.target.files[0])}
                  />
                  <CloudArrowUpIcon className="mx-auto h-12 w-12 text-gray-400 dark:text-gray-500 mb-4" />
                  {file ? (
                    <div className="flex items-center justify-center gap-2 text-primary-600 dark:text-primary-400 font-medium">
                      <span>{file.name}</span>
                      <span className="text-gray-500 text-sm">({(file.size / 1024 / 1024).toFixed(2)} MB)</span>
                    </div>
                  ) : (
                    <>
                      <p className="text-sm text-gray-600 dark:text-gray-300 font-medium">
                        Click to upload or drag and drop
                      </p>
                      <p className="text-xs text-gray-400 mt-1">
                        MP3, WAV, MP4, M4A (Max 25MB)
                      </p>
                    </>
                  )}
                </div>
              </div>
            )}

            <button
              type="submit"
              disabled={loading || (activeTab === 'youtube' && !url) || (activeTab === 'upload' && !file)}
              className="w-full btn-primary flex items-center justify-center gap-2 py-4 text-lg group"
            >
              {loading ? (
                <>
                  <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  Processing...
                </>
              ) : (
                <>
                  <SparklesIcon className="w-6 h-6 group-hover:animate-pulse-subtle" />
                  Generate Notes
                </>
              )}
            </button>
          </form>
        </div>
      </div>
    </div>
  )
}

export default InputSection
