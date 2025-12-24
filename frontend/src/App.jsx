import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Navbar from './components/Navbar';
import Dashboard from './pages/Dashboard';
import VoiceStudio from './pages/VoiceStudio';
import VideoStudio from './pages/VideoStudio';
import ConversationalAI from './pages/ConversationalAI';
import MultiAvatarStudio from './pages/MultiAvatarStudio';
import GlobalTranslation from './pages/GlobalTranslation';
import Settings from './pages/Settings';
import NotificationToast from './components/NotificationToast';
import { useAppStore } from './stores/appStore';

function App() {
  const { mode, notifications } = useAppStore();

  return (
    <BrowserRouter>
      <div className="app">
        <Navbar />
        <main className="main-content">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/voice-studio" element={<VoiceStudio />} />
            <Route path="/video-studio" element={<VideoStudio />} />
            <Route path="/conversational-ai" element={<ConversationalAI />} />
            <Route path="/multi-avatar" element={<MultiAvatarStudio />} />
            <Route path="/global-translation" element={<GlobalTranslation />} />
            <Route path="/settings" element={<Settings />} />
            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        </main>
        
        {/* Notifications */}
        <div className="notification-container">
          {notifications.map((notification) => (
            <NotificationToast key={notification.id} notification={notification} />
          ))}
        </div>
        
        {/* Mode Indicator */}
        <div className={`mode-indicator ${mode}`}>
          <span className="mode-dot"></span>
          <span className="mode-text">{mode === 'online' ? 'Online' : 'Sandbox'} Mode</span>
        </div>
      </div>
    </BrowserRouter>
  );
}

export default App;
