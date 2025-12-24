import React, { useState } from 'react';
import { useAppStore } from '../stores/appStore';
import { Settings as SettingsIcon, Key, Download, Trash2, HardDrive } from 'lucide-react';
import './Settings.css';

const Settings = () => {
  const { settings, updateSettings, mode, setMode } = useAppStore();
  const [apiKey, setApiKey] = useState(settings.elevenLabsApiKey);

  const handleSaveApiKey = () => {
    updateSettings({ elevenLabsApiKey: apiKey });
    useAppStore.getState().addNotification({
      type: 'success',
      title: 'Saved',
      message: 'API key saved successfully'
    });
  };

  const models = [
    { id: 'wav2lip', name: 'Wav2Lip', size: '3.2 GB', status: 'not_installed' },
    { id: 'coqui-xtts', name: 'Coqui XTTS-v2', size: '1.8 GB', status: 'not_installed' },
    { id: 'piper', name: 'Piper TTS', size: '450 MB', status: 'not_installed' },
    { id: 'sadtalker', name: 'SadTalker', size: '2.1 GB', status: 'not_installed' },
  ];

  return (
    <div className="settings-page">
      <div className="container">
        <header className="studio-header fade-in">
          <div>
            <h1 className="studio-title">
              <SettingsIcon size={40} className="title-icon" />
              Settings
            </h1>
            <p className="studio-subtitle">
              Configure API keys, manage models, and customize your experience
            </p>
          </div>
        </header>

        <div className="settings-content">
          {/* API Keys Section */}
          <section className="settings-section card-glass slide-up">
            <h2 className="section-header">
              <Key size={24} />
              API Keys
            </h2>
            
            <div className="input-wrapper">
              <label className="input-label">
                ElevenLabs API Key
                <span className="badge badge-warning" style={{ marginLeft: '0.5rem' }}>
                  Required for Online Mode
                </span>
              </label>
              <input
                type="password"
                className="input"
                value={apiKey}
                onChange={(e) => setApiKey(e.target.value)}
                placeholder="sk-..."
              />
              <p className="input-help">
                Get your API key from{' '}
                <a href="https://elevenlabs.io/app/settings/api-keys" target="_blank" rel="noopener noreferrer">
                  ElevenLabs Dashboard
                </a>
              </p>
            </div>

            <button className="btn btn-primary" onClick={handleSaveApiKey}>
              Save API Key
            </button>
          </section>

          {/* Mode Selection */}
          <section className="settings-section card-glass slide-up">
            <h2 className="section-header">
              <SettingsIcon size={24} />
              Operation Mode
            </h2>
            
            <div className="mode-selection">
              <button
                className={`mode-card ${mode === 'online' ? 'active' : ''}`}
                onClick={() => setMode('online')}
              >
                <div className="mode-icon">🌐</div>
                <h3>Online Mode</h3>
                <p>Use commercial APIs for premium quality</p>
                <ul className="mode-features">
                  <li>✓ ElevenLabs TTS</li>
                  <li>✓ High quality output</li>
                  <li>✓ Fast processing</li>
                  <li>✓ Latest models</li>
                </ul>
              </button>

              <button
                className={`mode-card ${mode === 'sandbox' ? 'active' : ''}`}
                onClick={() => setMode('sandbox')}
              >
                <div className="mode-icon">💻</div>
                <h3>Sandbox Mode</h3>
                <p>100% offline with open-source models</p>
                <ul className="mode-features">
                  <li>✓ Completely offline</li>
                  <li>✓ No API costs</li>
                  <li>✓ Privacy-focused</li>
                  <li>✓ Customizable models</li>
                </ul>
              </button>
            </div>
          </section>

          {/* Model Management */}
          <section className="settings-section card-glass slide-up">
            <h2 className="section-header">
              <HardDrive size={24} />
              Model Management
              <span className="badge badge-primary" style={{ marginLeft: '0.5rem' }}>
                Sandbox Mode
              </span>
            </h2>
            
            <p className="section-description">
              Download and manage open-source models for offline use
            </p>

            <div className="models-list">
              {models.map((model) => (
                <div key={model.id} className="model-item">
                  <div className="model-info">
                    <div className="model-name">{model.name}</div>
                    <div className="model-size">{model.size}</div>
                  </div>
                  
                  <div className="model-actions">
                    {model.status === 'not_installed' && (
                      <button className="btn btn-outline">
                        <Download size={18} />
                        Download
                      </button>
                    )}
                    {model.status === 'installed' && (
                      <>
                        <span className="badge badge-success">Installed</span>
                        <button className="btn btn-ghost">
                          <Trash2 size={18} />
                        </button>
                      </>
                    )}
                  </div>
                </div>
              ))}
            </div>
          </section>

          {/* Preferences */}
          <section className="settings-section card-glass slide-up">
            <h2 className="section-header">
              <SettingsIcon size={24} />
              Preferences
            </h2>

            <div className="input-wrapper">
              <label className="input-label">Default Language</label>
              <select className="select">
                <option value="en">English</option>
                <option value="es">Spanish</option>
                <option value="fr">French</option>
                <option value="de">German</option>
              </select>
            </div>

            <div className="input-wrapper">
              <label className="input-label">Theme</label>
              <select className="select" disabled>
                <option>Dark (Default)</option>
                <option>Light (Coming Soon)</option>
              </select>
            </div>
          </section>
        </div>
      </div>
    </div>
  );
};

export default Settings;
