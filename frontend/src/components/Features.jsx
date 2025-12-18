import React from 'react'
import { SparklesIcon, BoltIcon, ArrowDownTrayIcon, ShieldCheckIcon } from '@heroicons/react/24/outline'

function Features() {
    const features = [
        {
            icon: SparklesIcon,
            title: "Smart Summarization",
            description: "Get concise summaries that capture the essence of the content without the fluff."
        },
        {
            icon: BoltIcon,
            title: "Instant Key Points",
            description: "Automatically extract the most critical information and action items."
        },
        {
            icon: ArrowDownTrayIcon,
            title: "Multi-Format Export",
            description: "Download your notes in PDF or TXT format for easy sharing and storage."
        },
        {
            icon: ShieldCheckIcon,
            title: "Secure & Private",
            description: "Your data is processed securely and never used to train public models."
        }
    ]

    return (
        <section className="py-20 border-t border-gray-200 dark:border-slate-800 animate-fade-in">
            <div className="text-center mb-16">
                <h2 className="text-3xl font-display font-bold text-gray-900 dark:text-white mb-4">
                    Powerful Features
                </h2>
                <p className="text-gray-600 dark:text-gray-400 max-w-2xl mx-auto">
                    Everything you need to boost your productivity and learning.
                </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 px-4">
                {features.map((feature, index) => (
                    <div
                        key={index}
                        className="card p-6 hover:border-primary-500/50 transition-colors duration-300 group"
                    >
                        <div className="w-12 h-12 bg-primary-50 dark:bg-primary-900/20 rounded-xl flex items-center justify-center mb-4 group-hover:scale-110 transition-transform duration-300">
                            <feature.icon className="w-6 h-6 text-primary-600 dark:text-primary-400" />
                        </div>
                        <h3 className="text-lg font-bold text-gray-900 dark:text-white mb-2">
                            {feature.title}
                        </h3>
                        <p className="text-sm text-gray-600 dark:text-gray-400 leading-relaxed">
                            {feature.description}
                        </p>
                    </div>
                ))}
            </div>
        </section>
    )
}

export default Features
