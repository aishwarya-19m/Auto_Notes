import React from 'react'
import { LinkIcon, CpuChipIcon, DocumentTextIcon } from '@heroicons/react/24/outline'

function HowItWorks() {
    const steps = [
        {
            icon: LinkIcon,
            title: "Paste URL or Upload",
            description: "Simply paste a YouTube link or upload your audio file directly to the platform."
        },
        {
            icon: CpuChipIcon,
            title: "AI Analysis",
            description: "Our advanced AI models transcribe the audio and analyze the content structure."
        },
        {
            icon: DocumentTextIcon,
            title: "Get Smart Notes",
            description: "Instantly receive organized notes, key takeaways, and summaries ready for export."
        }
    ]

    return (
        <section className="py-20 animate-fade-in">
            <div className="text-center mb-16">
                <h2 className="text-3xl font-display font-bold text-gray-900 dark:text-white mb-4">
                    How It Works
                </h2>
                <p className="text-gray-600 dark:text-gray-400 max-w-2xl mx-auto">
                    Turn hours of content into minutes of reading in three simple steps.
                </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-8 relative px-4">
                {/* Connecting Line (Desktop) */}
                <div className="hidden md:block absolute top-12 left-[16%] right-[16%] h-0.5 bg-gradient-to-r from-gray-200 via-primary-200 to-gray-200 dark:from-slate-700 dark:via-slate-600 dark:to-slate-700 z-0"></div>

                {steps.map((step, index) => (
                    <div key={index} className="relative z-10 flex flex-col items-center text-center group">
                        <div className="w-24 h-24 rounded-2xl bg-white dark:bg-slate-800 border-2 border-gray-100 dark:border-slate-700 shadow-xl shadow-gray-200/50 dark:shadow-none mb-6 flex items-center justify-center transition-transform duration-300 group-hover:-translate-y-2">
                            <step.icon className="w-10 h-10 text-primary-500" />
                        </div>
                        <h3 className="text-xl font-bold text-gray-900 dark:text-white mb-3">
                            {step.title}
                        </h3>
                        <p className="text-gray-600 dark:text-gray-400 leading-relaxed px-4">
                            {step.description}
                        </p>
                    </div>
                ))}
            </div>
        </section>
    )
}

export default HowItWorks
