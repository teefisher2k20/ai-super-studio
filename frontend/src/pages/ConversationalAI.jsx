import React from 'react';
import { Bot } from 'lucide-react';

const ConversationalAI = () => {
  return (
    <div className="conversational-ai container" style={{ padding: '3rem 0' }}>
      <header className="studio-header fade-in">
        <div>
          <h1 className="studio-title">
            <Bot size={40} className="title-icon" />
            Conversational AI Agents
          </h1>
          <p className="studio-subtitle">
            Build intelligent AI agents with custom tools and real-time conversation
          </p>
        </div>
      </header>

      <div className="card-glass" style={{ padding: '2rem', marginTop: '2rem' }}>
        <h3>Create AI Agent</h3>
        
        <div className="input-wrapper">
          <label className="input-label">Agent Name</label>
          <input type="text" className="input" placeholder="My Customer Support Agent" />
        </div>

        <div className="input-wrapper">
          <label className="input-label">System Prompt</label>
          <textarea
            className="input textarea"
            rows="6"
            placeholder="You are a helpful customer support agent..."
          />
        </div>

        <div className="input-wrapper">
           <label className="input-label">Voice</label>
          <select className="select">
            <option>Rachel (Female, American)</option>
            <option>George (Male, British)</option>
            <option>Bella (Female, Gentle)</option>
          </select>
        </div>

        <button className="btn btn-primary">
          <Bot size={20} />
          <span>Create Agent</span>
        </button>
      </div>
    </div>
  );
};

export default ConversationalAI;
