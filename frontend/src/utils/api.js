import axios from 'axios';

const API_BASE_URL = '/api';

const api = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

// Request interceptor to add API key
api.interceptors.request.use((config) => {
    const apiKey = localStorage.getItem('elevenLabsApiKey');
    if (apiKey) {
        config.headers['X-API-Key'] = apiKey;
    }
    return config;
});

export const voiceAPI = {
    // Text-to-Speech
    generateSpeech: async (text, voice, model = 'eleven_multilingual_v2') => {
        const response = await api.post('/voice/generate', { text, voice, model });
        return response.data;
    },

    // Voice List
    getVoices: async () => {
        const response = await api.get('/voice/list');
        return response.data;
    },

    // Voice Cloning
    cloneVoice: async (formData) => {
        const response = await api.post('/voice/clone', formData, {
            headers: { 'Content-Type': 'multipart/form-data' },
        });
        return response.data;
    },
};

export const videoAPI = {
    // Generate AI Avatar Video
    generateVideo: async (formData) => {
        const response = await api.post('/video/generate', formData, {
            headers: { 'Content-Type': 'multipart/form-data' },
        });
        return response.data;
    },

    // Talking Photo
    generateTalkingPhoto: async (formData) => {
        const response = await api.post('/video/talking-photo', formData, {
            headers: { 'Content-Type': 'multipart/form-data' },
        });
        return response.data;
    },

    // Multi-Avatar Conversation
    generateMultiAvatar: async (script) => {
        const response = await api.post('/video/multi-avatar', { script });
        return response.data;
    },

    // Style Transfer
    applyStyleTransfer: async (videoId, style) => {
        const response = await api.post('/video/style-transfer', { videoId, style });
        return response.data;
    },
};

export const modelAPI = {
    // Get available models
    getAvailableModels: async () => {
        const response = await api.get('/models/available');
        return response.data;
    },

    // Get installed models
    getInstalledModels: async () => {
        const response = await api.get('/models/installed');
        return response.data;
    },

    // Download model
    downloadModel: async (modelId) => {
        const response = await api.post('/models/download', { modelId });
        return response.data;
    },

    // Delete model
    deleteModel: async (modelId) => {
        const response = await api.delete(`/models/${modelId}`);
        return response.data;
    },

    // Check download status
    getDownloadStatus: async (jobId) => {
        const response = await api.get(`/models/download-status/${jobId}`);
        return response.data;
    },
};

export const translationAPI = {
    // One-Click Global Content
    translateVideo: async (videoId, targetLanguages) => {
        const response = await api.post('/translation/global', {
            videoId,
            targetLanguages,
        });
        return response.data;
    },

    // Accent Transform
    transformAccent: async (audioId, targetAccent) => {
        const response = await api.post('/translation/accent', {
            audioId,
            targetAccent,
        });
        return response.data;
    },
};

export const conversationalAPI = {
    // Create AI Agent
    createAgent: async (config) => {
        const response = await api.post('/conversational/agent/create', config);
        return response.data;
    },

    // Test Agent
    testAgent: async (agentId, message) => {
        const response = await api.post('/conversational/agent/test', {
            agentId,
            message,
        });
        return response.data;
    },
};

export default api;
