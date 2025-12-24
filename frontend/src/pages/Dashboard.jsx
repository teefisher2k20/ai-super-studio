import React from 'react';
import { Link } from 'react-router-dom';
import { useAppStore } from '../stores/appStore';
import {
  Mic, Video, Users, Bot, Globe, Palette, Music, MessageSquare,
  Sparkles, Wand2, Languages, Github, Zap, TrendingUp
} from 'lucide-react';
import './Dashboard.css';

const Dashboard = () => {
  const { mode, projects } = useAppStore();

  const featureCards = [
    {
      icon: Mic,
      title: 'Voice Studio',
      description: 'Text-to-speech, voice cloning, and audio generation',
      link: '/voice-studio',
      gradient: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
      features: ['TTS Generation', 'Voice Cloning', 'Accent Transform']
    },
    {
      icon: Video,
      title: 'Video Studio',
      description: 'AI avatars, talking photos, and lip-sync videos',
      link: '/video-studio',
      gradient: 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
      features: ['AI Avatars', 'Talking Photos', 'Lip-Sync']
    },
    {
      icon: Users,
      title: 'Multi-Avatar',
      description: 'Create conversations with 2-4 AI avatars',
      link: '/multi-avatar',
      gradient: 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
      features: ['Conversations', 'Split Screen', 'Auto-Timing']
    },
    {
      icon: Bot,
      title: 'AI Agents',
      description: 'Build conversational AI agents with custom tools',
      link: '/conversational-ai',
      gradient: 'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)',
      features: ['Agent Builder', 'Custom Tools', 'Real-time']
    },
    {
      icon: Globe,
      title: 'Global Translation',
      description: 'Translate videos to 50+ languages with lip-sync',
      link: '/global-translation',
      gradient: 'linear-gradient(135deg, #fa709a 0%, #fee140 100%)',
      features: ['50+ Languages', 'Voice Cloning', 'Lip-sync Match']
    },
    {
      icon: Palette,
      title: 'Style Transfer',
      description: 'Apply artistic styles to avatars (anime, realistic, etc.)',
      link: '/video-studio',
      gradient: 'linear-gradient(135deg, #30cfd0 0%, #330867 100%)',
      features: ['Multiple Styles', 'Real-time Preview', '1080p Output']
    }
  ];

  const innovativeFeatures = [
    { icon: Music, text: 'Music Video Generator' },
    { icon: MessageSquare, text: 'Interactive Chatbots' },
    { icon: Wand2, text: 'Voice-to-Character' },
    { icon: Languages, text: 'Sign Language Avatars' },
    { icon: Sparkles, text: 'Emotion Transfer' },
    { icon: Github, text: 'Open Source Models' },
    { icon: Zap, text: 'Real-Time Puppeteering' },
    { icon: TrendingUp, text: 'AI Analytics' },
  ];

  const stats = [
    { label: 'Total Projects', value: projects.length },
    { label: 'Features', value: '40+' },
    { label: 'Models', value: mode === 'online' ? '5+' : '15+' },
    { label: 'Languages', value: '50+' }
  ];

  return (
    <div className="dashboard">
      <div className="container">
        {/* Hero Section */}
        <section className="hero fade-in">
          <h1 className="hero-title">
            Welcome to <span className="gradient-text">AI Super Studio</span>
          </h1>
          <p className="hero-subtitle">
            The ultimate AI-powered platform combining voice and video generation with 40+ innovative features
          </p>
          <div className="hero-mode-badge">
            <span className={`mode-badge ${mode}`}>
              {mode === 'online' ? '🌐 Online Mode' : '💻 Sandbox Mode'}
            </span>
            <p>
              {mode === 'online' 
                ? 'Using commercial APIs for premium quality'
                : 'Running 100% offline with open-source models'}
            </p>
          </div>
        </section>

        {/* Stats */}
        <section className="stats-section slide-up">
          <div className="stats-grid">
            {stats.map((stat, index) => (
              <div key={index} className="stat-card card-glass">
                <div className="stat-value gradient-text">{stat.value}</div>
                <div className="stat-label">{stat.label}</div>
              </div>
            ))}
          </div>
        </section>

        {/* Feature Cards */}
        <section className="features-section">
          <h2 className="section-title">Core Features</h2>
          <div className="features-grid">
            {featureCards.map((card, index) => {
              const Icon = card.icon;
              return (
                <Link 
                  key={index} 
                  to={card.link} 
                  className="feature-card scale-in"
                  style={{ animationDelay: `${index * 0.1}s` }}
                >
                  <div className="feature-card-header" style={{ background: card.gradient }}>
                    <Icon size={32} />
                  </div>
                  <div className="feature-card-body">
                    <h3>{card.title}</h3>
                    <p>{card.description}</p>
                    <ul className="feature-list">
                      {card.features.map((feature, i) => (
                        <li key={i}>• {feature}</li>
                      ))}
                    </ul>
                  </div>
                </Link>
              );
            })}
          </div>
        </section>

        {/* Innovative Features */}
        <section className="innovative-section">
          <h2 className="section-title">Innovative Features</h2>
          <div className="innovative-grid">
            {innovativeFeatures.map((feature, index) => {
              const Icon = feature.icon;
              return (
                <div key={index} className="innovative-item">
                  <Icon size={24} className="innovative-icon" />
                  <span>{feature.text}</span>
                </div>
              );
            })}
          </div>
        </section>

        {/* Recent Projects */}
        {projects.length > 0 && (
          <section className="projects-section">
            <h2 className="section-title">Recent Projects</h2>
            <div className="projects-grid">
              {projects.slice(0, 4).map((project) => (
                <div key={project.id} className="project-card card">
                  <div className="project-type">{project.type}</div>
                  <div className="project-name">{project.name}</div>
                  <div className="project-date">
                    {new Date(project.createdAt).toLocaleDateString()}
                  </div>
                </div>
              ))}
            </div>
          </section>
        )}

        {/* Getting Started */}
        {projects.length === 0 && (
          <section className="getting-started card-glass">
            <h2>🚀 Getting Started</h2>
            <p>Ready to create amazing AI-powered content? Here's what you can do:</p>
            <ol>
              <li>
                <strong>Configure Settings:</strong> Add your API keys in <Link to="/settings">Settings</Link> for online mode
              </li>
              <li>
                <strong>Try Voice Studio:</strong> Generate speech from text or clone your voice
              </li>
              <li>
                <strong>Create Videos:</strong> Upload a photo and make it talk with AI
              </li>
              <li>
                <strong>Go Global:</strong> Translate your content to 50+ languages instantly
              </li>
            </ol>
          </section>
        )}
      </div>
    </div>
  );
};

export default Dashboard;
