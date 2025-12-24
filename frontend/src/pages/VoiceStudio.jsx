import React, { useState } from 'react';
import { useAppStore } from '../stores/appStore';
import { voiceAPI } from '../utils/api';
import { Play, Download, Upload, Mic, Volume2, Wand2 } from 'lucide-react';
import './VoiceStudio.css';

const VoiceStudio = () => {
  const { mode, addNotification, setIsGenerating } = useAppStore();
  const [text, setText] = useState('');
  const [selectedVoice, setSelectedVoice] = useState('');
  const [selectedModel, setSelectedModel] = useState('eleven_multilingual_v2');
  const [generatedAudio, setGeneratedAudio] = useState(null);
  const [voices, setVoices] = useState([]);
  const [activeTab, setActiveTab] = useState('tts'); // tts, clone, accent

  const handleGenerate = async () => {
    if (!text.trim()) {
      addNotification({
        type: 'error',
        title: 'Error',
        message: 'Please enter text to generate speech'
      });
      return;
    }

    try {
      setIsGenerating(true);
      const result = await voiceAPI.generateSpeech(text, selectedVoice, selectedModel);
      setGeneratedAudio(result.audioUrl);
      
      addNotification({
        type: 'success',
        title: 'Success',
        message: 'Speech generated successfully'
      });
    } catch (error) {
      addNotification({
        type: 'error',
        title: 'Generation Failed',
        message: error.message || 'Failed to generate speech'
      });
    } finally {
      setIsGenerating(false);
    }
  };

  const handleVoiceClone = async (files) => {
    const formData = new FormData();
    files.forEach((file, index) => {
      formData.append(`sample_${index}`, file);
    });

    try {
      setIsGenerating(true);
      const result = await voiceAPI.cloneVoice(formData);
      
      addNotification({
        type: 'success',
        title: 'Voice Cloned',
        message: `Voice "${result.voiceName}" created successfully`
      });
    } catch (error) {
      addNotification({
        type: 'error',
        title: 'Cloning Failed',
        message: error.message
      });
    } finally {
      setIsGenerating(false);
    }
  };

  return (
    <div className="voice-studio">
      <div className="container">
        <header className="studio-header fade-in">
          <div>
            <h1 className="studio-title">
              <Volume2 size={40} className="title-icon" />
              Voice Studio
            </h1>
            <p className="studio-subtitle">
              Generate speech, clone voices, and transform accents with AI
            </p>
          </div>
          <div className="mode-indicator-small">
            {mode === 'online' ? '🌐 Online' : '💻 Sandbox'}
          </div>
        </header>

        {/* Tab Navigation */}
        <div className="tabs">
          <button 
            className={`tab ${activeTab === 'tts' ? 'active' : ''}`}
            onClick={() => setActiveTab('tts')}
          >
            <Mic size={20} />
            Text-to-Speech
          </button>
          <button 
            className={`tab ${activeTab === 'clone' ? 'active' : ''}`}
            onClick={() => setActiveTab('clone')}
          >
            <Upload size={20} />
            Voice Cloning
          </button>
          <button 
            className={`tab ${activeTab === 'accent' ? 'active' : ''}`}
            onClick={() => setActiveTab('accent')}
          >
            <Wand2 size={20} />
            Accent Transform
          </button>
        </div>

        {/* Text-to-Speech Tab */}
        {activeTab === 'tts' && (
          <div className="studio-content slide-up">
            <div className="content-grid">
              <div className="input-panel card-glass">
                <h3>Input</h3>
                
                <div className="input-wrapper">
                  <label className="input-label">Text to Generate</label>
                  <textarea
                    className="input textarea"
                    rows="8"
                    value={text}
                    onChange={(e) => setText(e.target.value)}
                    placeholder="Enter the text you want to convert to speech..."
                  />
                  <div className="char-count">
                    {text.length} characters
                  </div>
                </div>

                <div className="input-wrapper">
                  <label className="input-label">Voice Model</label>
                  <select 
                    className="select"
                    value={selectedModel}
                    onChange={(e) => setSelectedModel(e.target.value)}
                  >
                    <option value="eleven_multilingual_v2">Multilingual v2 (Best Quality)</option>
                    <option value="eleven_flash_v2_5">Flash v2.5 (Fast & Cheap)</option>
                    <option value="eleven_turbo_v2_5">Turbo v2.5 (Balanced)</option>
                    {mode === 'sandbox' && (
                      <>
                        <option value="coqui_xtts">Coqui XTTS (Offline)</option>
                        <option value="piper">Piper TTS (Offline)</option>
                        <option value="bark">Bark (Expressive, Offline)</option>
                      </>
                    )}
                  </select>
                </div>

                <div className="input-wrapper">
                  <label className="input-label">Voice</label>
                  <select 
                    className="select"
                    value={selectedVoice}
                    onChange={(e) => setSelectedVoice(e.target.value)}
                  >
                    <option value="">Select a voice...</option>
                    <option value="rachel">Rachel (Female, American)</option>
                    <option value="george">George (Male, British)</option>
                    <option value="bella">Bella (Female, Gentle)</option>
                    <option value="adam">Adam (Male, Deep)</option>
                  </select>
                </div>

                <button className="btn btn-primary" onClick={handleGenerate}>
                  <Play size={20} />
                  <span>Generate Speech</span>
                </button>
              </div>

              <div className="output-panel card-glass">
                <h3>Output</h3>
                
                {generatedAudio ? (
                  <div className="audio-output">
                    <div className="waveform-visualizer">
                      <div className="waveform-bars">
                        {[...Array(40)].map((_, i) => (
                          <div key={i} className="wave-bar"></div>
                        ))}
                      </div>
                    </div>
                    
                    <audio controls className="audio-player">
                      <source src={generatedAudio} type="audio/mpeg" />
                    </audio>

                    <div className="output-actions">
                      <button className="btn btn-secondary">
                        <Play size={20} />
                        <span>Play</span>
                      </button>
                      <button className="btn btn-secondary">
                        <Download size={20} />
                        <span>Download</span>
                      </button>
                    </div>
                  </div>
                ) : (
                  <div className="placeholder-state">
                    <Volume2 size={64} className="placeholder-icon" />
                    <p>Your generated audio will appear here</p>
                  </div>
                )}
              </div>
            </div>
          </div>
        )}

        {/* Voice Cloning Tab */}
        {activeTab === 'clone' && (
          <div className="studio-content slide-up">
            <div className="clone-panel card-glass">
              <h3>Clone Your Voice</h3>
              <p className="panel-description">
                Upload 2-3 audio samples (each 30+ seconds) of your voice to create a clone
              </p>
              
              <div className="upload-zone">
                <Upload size={48} />
                <p>Drag & drop audio files or click to browse</p>
                <span className="upload-hint">Supported: MP3, WAV, M4A</span>
              </div>

              <div className="input-wrapper">
                <label className="input-label">Voice Name</label>
                <input 
                  type="text"
                  className="input"
                  placeholder="e.g., My Voice Clone"
                />
              </div>

              <button className="btn btn-primary">
                <Wand2 size={20} />
                <span>Create Voice Clone</span>
              </button>
            </div>
          </div>
        )}

        {/* Accent Transform Tab */}
        {activeTab === 'accent' && (
          <div className="studio-content slide-up">
            <div className="accent-panel card-glass">
              <h3>Accent Transformer</h3>
              <p className="panel-description">
                Transform your voice to different accents while keeping your unique characteristics
              </p>
              
              <div className="accent-grid">
                {['British', 'Australian', 'Indian', 'Southern US', 'New York', 'Scottish'].map((accent) => (
                  <button key={accent} className="accent-card">
                    <div className="accent-flag">🎭</div>
                    <span>{accent}</span>
                  </button>
                ))}
              </div>

              <div className="input-wrapper">
                <label className="input-label">Upload Audio</label>
                <div className="upload-zone-small">
                  <Upload size={24} />
                  <span>Choose audio file</span>
                </div>
              </div>

              <button className="btn btn-primary">
                <Wand2 size={20} />
                <span>Transform Accent</span>
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default VoiceStudio;
