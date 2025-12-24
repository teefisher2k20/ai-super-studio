import React from 'react';
import { Users } from 'lucide-react';

const MultiAvatarStudio = () => {
  return (
    <div className="multi-avatar-studio container" style={{ padding: '3rem 0' }}>
      <header className="studio-header fade-in">
        <div>
          <h1 className="studio-title">
            <Users size={40} className="title-icon" />
            Multi-Avatar Conversations
          </h1>
          <p className="studio-subtitle">
            Create videos with 2-4 AI avatars having natural conversations
          </p>
        </div>
      </header>

      <div className="card-glass" style={{ padding: '2rem', marginTop: '2rem' }}>
        <h3>Script Format</h3>
        <p className="panel-description">
          Write your script with character labels (e.g., "ALICE: Hello there")
        </p>
        
        <textarea
          className="input textarea"
          rows="12"
          placeholder="ALICE: Hello! Welcome to our show.&#10;BOB: Thanks for having me, Alice!&#10;ALICE: Today we're discussing AI technology.&#10;BOB: It's fascinating how far we've come..."
          style={{ marginBottom: '1.5rem' }}
        />

        <button className="btn btn-primary">
          <Users size={20} />
          <span>Generate Multi-Avatar Video</span>
        </button>
      </div>
    </div>
  );
};

export default MultiAvatarStudio;
