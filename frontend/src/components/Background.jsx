import React from 'react'

function Background() {
    return (
        <div className="fixed inset-0 z-0 pointer-events-none overflow-hidden bg-gray-50 dark:bg-dark-bg transition-colors duration-300">
            {/* Grid Pattern Overlay */}
            <div
                className="absolute inset-0 opacity-[0.4] dark:opacity-[0.2]"
                style={{
                    backgroundImage: `linear-gradient(#6366f1 1px, transparent 1px), linear-gradient(to right, #6366f1 1px, transparent 1px)`,
                    backgroundSize: '4rem 4rem',
                    maskImage: 'radial-gradient(circle at center, black 40%, transparent 100%)',
                    WebkitMaskImage: 'radial-gradient(circle at center, black 40%, transparent 100%)'
                }}
            ></div>

            {/* Animated Orbs */}
            <div className="absolute top-[-10%] left-[-10%] w-[50%] h-[50%] bg-purple-500/30 dark:bg-purple-900/20 rounded-full blur-[120px] animate-pulse-subtle mix-blend-multiply dark:mix-blend-screen"></div>
            <div className="absolute top-[20%] right-[-10%] w-[40%] h-[60%] bg-indigo-500/30 dark:bg-indigo-900/20 rounded-full blur-[120px] animate-pulse-subtle mix-blend-multiply dark:mix-blend-screen" style={{ animationDelay: '2s' }}></div>
            <div className="absolute bottom-[-10%] left-[20%] w-[60%] h-[40%] bg-blue-500/30 dark:bg-blue-900/20 rounded-full blur-[120px] animate-pulse-subtle mix-blend-multiply dark:mix-blend-screen" style={{ animationDelay: '4s' }}></div>
        </div>
    )
}

export default Background
