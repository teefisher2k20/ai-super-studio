# Installation Guide

## Prerequisites

### System Requirements

**Online Mode:**

- OS: Windows, macOS, or Linux
- RAM: 4GB minimum
- Storage: 2GB
- Python: 3.8 or higher
- Node.js: 16.x or higher
- Internet connection: Required

**Sandbox Mode:**

- OS: Windows, macOS, or Linux
- RAM: 16GB minimum (32GB recommended)
- Storage: 50GB+ for all models
- Python: 3.10 or higher
- Node.js: 16.x or higher
- GPU: NVIDIA GPU with 8GB+ VRAM (recommended)
- CUDA: 11.8 or higher (for GPU acceleration)
- Internet: Only for initial model downloads

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-super-studio.git
cd ai-super-studio
```

### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
copy .env.example .env  # Windows
# OR
cp .env.example .env    # macOS/Linux

# Edit .env and add your ElevenLabs API key
# ELEVENLABS_API_KEY=your_api_key_here

# Start the server
python app.py
```

The backend will start on `http://localhost:5000`

### 3. Frontend Setup

Open a new terminal window:

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

The frontend will start on `http://localhost:5173`

## Detailed Installation

### Installing Python Dependencies

The `requirements.txt` includes:

- **Flask**: Web framework
- **elevenlabs**: Official ElevenLabs SDK
- **TTS (Coqui)**: Open-source text-to-speech
- **torch**: PyTorch for deep learning models
- **opencv-python**: Computer vision library for video processing
- **transformers**: Hugging Face transformers library

Note: Installing PyTorch with CUDA support requires additional steps. Visit [pytorch.org](https://pytorch.org/) for platform-specific installation instructions.

### Installing Node.js Dependencies

The `package.json` includes:

- **React 18**: Frontend framework
- **Vite**: Build tool  
- **React Router**: Routing
- **Axios**: HTTP client
- **Zustand**: State management
- **Lucide React**: Icon library

## Configuration

### API Keys

1. **ElevenLabs API Key** (Required for Online Mode)
   - Visit <https://elevenlabs.io/app/settings/api-keys>
   - Generate a new API key
   - Add to backend `.env` file:

     ```
     ELEVENLABS_API_KEY=sk-your-key-here
     ```

   - Or configure in the app Settings page

### Environment Variables

Backend (`.env`):

```env
ELEVENLABS_API_KEY=your_api_key_here
DEBUG=True
PORT=5000
MODE=online
MODELS_DIR=./models
```

## Installing Open-Source Models (Sandbox Mode)

### Method 1: Through the Application

1. Start the application
2. Go to Settings > Model Management
3. Click "Download" for each model you want
4. Wait for downloads to complete

### Method 2: Manual Installation

#### Coqui XTTS-v2

```bash
pip install TTS
python -c "from TTS.api import TTS; TTS('tts_models/multilingual/multi-dataset/xtts_v2')"
```

#### Piper TTS

```bash
pip install piper-tts
# Download models from https://github.com/rhasspy/piper/releases
```

#### Bark

```bash
pip install git+https://github.com/suno-ai/bark.git
```

#### Wav2Lip

```bash
git clone https://github.com/Rudrabha/Wav2Lip.git backend/models/wav2lip
cd backend/models/wav2lip
pip install -r requirements.txt
# Download pretrained models as per repository instructions
```

#### SadTalker

```bash
git clone https://github.com/OpenTalker/SadTalker.git backend/models/sadtalker
cd backend/models/sadtalker
pip install -r requirements.txt
# Download checkpoints as per repository instructions
```

## Platform-Specific Instructions

### Windows

1. Install Python from python.org
2. Install Node.js from nodejs.org
3. Install Git from git-scm.com
4. (Optional) Install CUDA Toolkit for GPU support
5. Run PowerShell as Administrator for some commands

### macOS

```bash
# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python@3.10

# Install Node.js
brew install node

# Install Git
brew install git
```

### Linux (Ubuntu/Debian)

```bash
# Update package list
sudo apt update

# Install Python
sudo apt install python3.10 python3-pip python3-venv

# Install Node.js
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs

# Install Git
sudo apt install git

# Install build tools (required for some Python packages)
sudo apt install build-essential

# For GPU support
# Install NVIDIA drivers and CUDA toolkit
```

## Verification

### Check Backend

```bash
curl http://localhost:5000/api/health
```

Expected response:

```json
{
  "status": "healthy",
  "version": "1.0.0",
  "services": {
    "voice": "ready",
    "video": "ready",
    "models": "ready"
  }
}
```

### Check Frontend

Visit `http://localhost:5173` in your browser. You should see the AI Super Studio dashboard.

## Troubleshooting

### Backend Won't Start

**Problem**: `ModuleNotFoundError`
**Solution**:

```bash
pip install -r requirements.txt
```

**Problem**: Port 5000 already in use
**Solution**: Change PORT in `.env` or stop the conflicting process

### Frontend Won't Start

**Problem**: `npm install` fails
**Solution**:

```bash
rm -rf node_modules package-lock.json
npm cache clean --force
npm install
```

**Problem**: Port 5173 already in use
**Solution**: Vite will automatically try the next available port

### Models Not Loading

**Problem**: CUDA out of memory
**Solution**:

- Reduce batch size
- Use CPU mode (slower)
- Get more VRAM

**Problem**: Model download fails
**Solution**:

- Check internet connection
- Ensure sufficient disk space
- Try manual installation

### API Errors

**Problem**: "Invalid API key"
**Solution**:

- Verify API key is correct in `.env` or Settings
- Check key hasn't expired
- Ensure no extra spaces in the key

**Problem**: "Rate limit exceeded"
**Solution**:

- Wait before retrying
- Upgrade ElevenLabs plan
- Switch to Sandbox mode

## Next Steps

- Read the [Features Guide](FEATURES.md)
- Check out the [Sandbox Guide](SANDBOX_GUIDE.md)
- Explore the [API Documentation](API_DOCUMENTATION.md)
- Join our community on Discord

## Support

- GitHub Issues: <https://github.com/yourusername/ai-super-studio/issues>
- Discord: <https://discord.gg/ai-super-studio>
- Email: <support@aisuperstudio.com>
