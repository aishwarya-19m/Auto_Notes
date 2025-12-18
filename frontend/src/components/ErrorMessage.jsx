import React from 'react'
import { XCircleIcon, XMarkIcon } from '@heroicons/react/24/outline'

function ErrorMessage({ message, onDismiss }) {
  if (!message) return null

  return (
    <div className="fixed bottom-6 right-6 z-50 animate-slide-up max-w-md w-full">
      <div className="bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-800/50 rounded-xl p-4 shadow-lg shadow-red-500/10 flex items-start gap-3">
        <XCircleIcon className="w-6 h-6 text-red-500 flex-shrink-0 mt-0.5" />
        <div className="flex-1">
          <h3 className="text-sm font-semibold text-red-800 dark:text-red-200">Error Occurred</h3>
          <p className="text-sm text-red-600 dark:text-red-300 mt-1">{message}</p>
        </div>
        <button
          onClick={onDismiss}
          className="text-red-400 hover:text-red-600 dark:hover:text-red-200 transition-colors"
        >
          <XMarkIcon className="w-5 h-5" />
        </button>
      </div>
    </div>
  )
}

export default ErrorMessage
