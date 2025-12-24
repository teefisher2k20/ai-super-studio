import React from 'react';
import { Globe } from 'lucide-react';

const GlobalTranslation = () => {
  return (
    <div className="global-translation container" style={{ padding: '3rem 0' }}>
      <header className="studio-header fade-in">
        <div>
          <h1 className="studio-title">
            <Globe size={40} className="title-icon" />
            Global Translation
          </h1>
          <p className="studio-subtitle">
            Translate videos to 50+ languages with perfect lip-sync
          </p>
        </div>
      </header>

      <div className="card-glass" style={{ padding: '2rem', marginTop: '2rem' }}>
        <h3>One-Click Global Content</h3>
        <p className="panel-description">
          Upload a video and translate it to multiple languages simultaneously
        </p>

        <div className="upload-zone" style={{ marginBottom: '2rem' }}>
          <Globe size={48} />
          <p>Upload video to translate</p>
          <span className="upload-hint">MP4, MOV - Max 500MB</span>
        </div>

        <div className="input-wrapper">
          <label className="input-label">Target Languages</label>
          <div className="language-tags" style={{ display: 'flex', flexWrap: 'wrap', gap: '0.5rem', marginTop: '0.5rem' }}>
            {['Spanish', 'French', 'German', 'Chinese', 'Japanese', 'Arabic'].map((lang) => (
              <span key={lang} className="badge badge-primary" style={{ cursor: 'pointer' }}>
                {lang} ×
              </span>
            ))}
          </div>
        </div>

        <button className="btn btn-primary">
          <Globe size={20} />
          <span>Translate Video</span>
        </button>
      </div>
    </div>
  );
};

export default GlobalTranslation;
