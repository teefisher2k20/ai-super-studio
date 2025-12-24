import { create } from 'zustand';

export const useAppStore = create((set) => ({
    // Mode: 'online' or 'sandbox'
    mode: localStorage.getItem('mode') || 'online',
    setMode: (mode) => {
        localStorage.setItem('mode', mode);
        set({ mode });
    },

    // Settings
    settings: {
        elevenLabsApiKey: localStorage.getItem('elevenLabsApiKey') || '',
        theme: 'dark',
        language: 'en',
    },
    updateSettings: (newSettings) =>
        set((state) => {
            const updated = { ...state.settings, ...newSettings };
            if (newSettings.elevenLabsApiKey !== undefined) {
                localStorage.setItem('elevenLabsApiKey', newSettings.elevenLabsApiKey);
            }
            return { settings: updated };
        }),

    // Projects
    projects: [],
    addProject: (project) =>
        set((state) => ({
            projects: [...state.projects, { ...project, id: Date.now(), createdAt: new Date() }],
        })),
    deleteProject: (id) =>
        set((state) => ({
            projects: state.projects.filter((p) => p.id !== id),
        })),

    // Models (for sandbox mode)
    installedModels: [],
    setInstalledModels: (models) => set({ installedModels: models }),

    // Generation state
    isGenerating: false,
    generationProgress: 0,
    setIsGenerating: (isGenerating) => set({ isGenerating }),
    setGenerationProgress: (progress) => set({ generationProgress: progress }),

    // Notifications
    notifications: [],
    addNotification: (notification) =>
        set((state) => ({
            notifications: [
                ...state.notifications,
                { ...notification, id: Date.now() },
            ],
        })),
    removeNotification: (id) =>
        set((state) => ({
            notifications: state.notifications.filter((n) => n.id !== id),
        })),
}));
