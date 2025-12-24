import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { useAppStore } from '../stores/appStore';
import { 
  Home, Mic, Video, Bot, Users, Globe, Settings as SettingsIcon, 
  Sparkles 
} from 'lucide-react';
import './Navbar.css';

const Navbar = () => {
  const location = useLocation();
  const { mode, setMode } = useAppStore();

  const navItems = [
    { path: '/', label: 'Dashboard', icon: Home },
    { path: '/voice-studio', label: 'Voice Studio', icon: Mic },
    { path: '/video-studio', label: 'Video Studio', icon: Video },
    { path: '/multi-avatar', label: 'Multi-Avatar', icon: Users },
    { path: '/conversational-ai', label: 'AI Agents', icon: Bot },
    { path: '/global-translation', label: 'Translation', icon: Globe },
    { path: '/settings', label: 'Settings', icon: SettingsIcon },
  ];

  const toggleMode = () => {
    setMode(mode === 'online' ? 'sandbox' : 'online');
  };

  return (
    <nav className="navbar glass">
      <div className="navbar-container">
        <Link to="/" className="navbar-brand">
          <Sparkles size={32} className="brand-icon" />
          <span className="brand-text gradient-text">AI Super Studio</span>
        </Link>

        <div className="navbar-nav">
          {navItems.map((item) => {
            const Icon = item.icon;
            const isActive = location.pathname === item.path;
            
            return (
              <Link
                key={item.path}
                to={item.path}
                className={`nav-item ${isActive ? 'active' : ''}`}
              >
                <Icon size={20} />
                <span>{item.label}</span>
              </Link>
            );
          })}
        </div>

        <div className="navbar-actions">
          <button className="mode-toggle-btn" onClick={toggleMode}>
            <div className={`toggle-indicator ${mode}`}>
              <span className="toggle-option">{mode === 'online' ? '🌐' : '💻'}</span>
            </div>
            <span className="mode-label">{mode === 'online' ? 'Online' : 'Sandbox'}</span>
          </button>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
