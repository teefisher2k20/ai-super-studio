import React, { useState } from 'react';
import { useAppStore } from '../stores/appStore';
import { videoAPI } from '../utils/api';
import { Video, Upload, Wand2, Play, Download } from 'lucide-react';
import './VideoStudio.css';

const VideoStudio = () => {
  const { mode, addNotification } = useAppStore();
  const [activeTab, setActiveTab] = useState('avatar'); // avatar, talking-photo, style

  return (
    <div className="video-studio">
      <div className="container">
        <header className="studio-header fade-in">
          <div>
            <h1 className="studio-title">
              <Video size={40} className="title-icon" />
              Video Studio
            </h1>
            <p className="studio-subtitle">
              Create AI avatars, talking photos, and apply artistic styles
            </p>
          </div>
          <div className="mode-indicator-small">
            {mode === 'online' ? '🌐 Online' : '💻 Sandbox'}
          </div>
        </header>

        <div className="tabs">
          <button 
            className={`tab ${activeTab === 'avatar' ? 'active' : ''}`}
            onClick={() => setActiveTab('avatar')}
          >
            <Video size={20} />
            AI Avatar
          </button>
          <button 
            className={`tab ${activeTab === 'talking-photo' ? 'active' : ''}`}
            onClick={() => setActiveTab('talking-photo')}
          >
            <Upload size={20} />
            Talking Photo
          </button>
          <button 
            className={`tab ${activeTab === 'style' ? 'active' : ''}`}
            onClick={() => setActiveTab('style')}
          >
            <Wand2 size={20} />
            Style Transfer
          </button>
        </div>

        {activeTab === 'avatar' && (
          <div className="studio-content slide-up">
            <div className="content-grid">
              <div className="input-panel card-glass">
                <h3>Create AI Avatar Video</h3>
                
                <div className="input-wrapper">
                  <label className="input-label">Script</label>
                  <textarea
                    className="input textarea"
                    rows="6"
                    placeholder="Enter the script for your avatar to speak..."
                  />
                </div>

                <div className="input-wrapper">
                  <label className="input-label">Avatar Style</label>
                  <select className="select">
                    <option>Professional Female</option>
                    <option>Professional Male</option>
                    <option>Casual Young Adult</option>
                    <option>Custom Upload</option>
                  </select>
                </div>

                <button className="btn btn-primary">
                  <Play size={20} />
                  <span>Generate Video</span>
                </button>
              </div>

              <div className="output-panel card-glass">
                <h3>Preview</h3>
                <div className="placeholder-state">
                  <Video size={64} className="placeholder-icon" />
                  <p>Your generated video will appear here</p>
                </div>
              </div>
            </div>
          </div>
        )}

        {activeTab === 'talking-photo' && (
          <div className="studio-content slide-up">
            <div className="talking-photo-panel card-glass">
              <h3>Talking Photo Generator</h3>
              <p className="panel-description">
                Upload a photo and make it talk with your voice or text
              </p>

              <div className="upload-zone">
                <Upload size={48} />
                <p>Upload a portrait photo</p>
                <span className="upload-hint">JPG, PNG - Max 10MB</span>
              </div>

              <div className="input-wrapper">
                <label className="input-label">Audio or Text</label>
                <textarea
                  className="input textarea"
                  rows="4"
                  placeholder="Enter text or upload audio file..."
                />
              </div>

              <button className="btn btn-primary">
                <Wand2 size={20} />
                <span>Generate Talking Photo</span>
              </button>
            </div>
          </div>
        )}

        {activeTab === 'style' && (
          <div className="studio-content slide-up">
            <div className="style-panel card-glass">
              <h3>Style Transfer</h3>
              <p className="panel-description">
                Apply artistic styles to your avatar videos
              </p>

              <div className="style-grid">
                {['Realistic', 'Anime', 'Pixar', 'Comic', 'Oil Painting', 'Watercolor'].map((style) => (
                  <button key={style} className="style-card">
                    <div className="style-preview">🎨</div>
                    <span>{style}</span>
                  </button>
                ))}
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default VideoStudio;
