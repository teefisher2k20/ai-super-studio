# Quick Start Guide

Get AI Super Studio running in 5 minutes!

## Prerequisites Check

Before starting, ensure you have:

- [ ] Python 3.8+ installed (`python --version`)
- [ ] Node.js 16+ installed (`node --version`)
- [ ] Git installed (`git --version`)
- [ ] 4GB+ free RAM
- [ ] 2GB+ free disk space

## Installation (3 Steps)

### Step 1: Get the Code

Choose one:

**Option A: Clone from GitHub** (recommended)

```bash
git clone https://github.com/yourusername/ai-super-studio.git
cd ai-super-studio
```

**Option B: Download ZIP**
Download and extract the ZIP file, then open terminal in the extracted folder.

### Step 2: Run Setup

**Windows:**

```cmd
setup.bat
```

**macOS/Linux:**

```bash
chmod +x setup.sh
./setup.sh
```

This will:

- Create Python virtual environment
- Install all dependencies
- Set up project directories
- Create configuration files

**⏱️ Estimated time: 3-5 minutes**

### Step 3: Configure API Key

1. Get your ElevenLabs API key:
   - Go to <https://elevenlabs.io/app/settings/api-keys>
   - Click "Create New Key"
   - Copy the key

2. Add it to the configuration:
   - Open `backend/.env` in a text editor
   - Find the line: `ELEVENLABS_API_KEY=your_api_key_here`
   - Replace `your_api_key_here` with your actual key
   - Save the file

**Skip this step if you want to use Sandbox mode only**

## Running the Application

**Windows:**

```cmd
start.bat
```

**macOS/Linux:**

```bash
./start.sh
```

**Or manually in two terminals:**

Terminal 1 (Backend):

```bash
cd backend
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
python app.py
```

Terminal 2 (Frontend):

```bash
cd frontend
npm run dev
```

## Access the Application

Open your browser and go to:

- **Frontend**: <http://localhost:5173>
- **Backend API**: <http://localhost:5000/api/health>

## First Steps in the App

1. **Dashboard**: View all available features
2. **Settings**: Configure your API key (if using online mode)
3. **Voice Studio**: Try generating your first speech
4. **Video Studio**: Create a talking photo

## Quick Test

Try this in Voice Studio:

1. Go to Voice Studio
2. Enter text: "Hello! This is my first AI-generated speech."
3. Select a voice (e.g., "Rachel")
4. Click "Generate Speech"
5. Listen to the result!

## Troubleshooting

### Port Already in Use

If you see "port already in use":

- Backend: Change `PORT=5000` to `PORT=5001` in `backend/.env`
- Frontend: Vite will auto-select next available port

### Dependencies Install Failed

```bash
# Backend
cd backend
pip install --upgrade pip
pip install -r requirements.txt

# Frontend
cd frontend
rm -rf node_modules package-lock.json
npm install
```

### API Key Not Working

- Check for extra spaces in `.env` file
- Verify key is valid on ElevenLabs dashboard
- Restart backend server after changing `.env`

### GPU Not Detected (Sandbox Mode)

This is normal if you don't have NVIDIA GPU. The app will use CPU mode (slower but works).

## What's Next?

- **Read Feature Docs**: See [FEATURES.md](docs/FEATURES.md) for detailed feature explanations
- **Try Sandbox Mode**: Switch to offline mode in Settings
- **Download Models**: In Settings > Model Management
- **Explore Examples**: Check out each studio section

## Getting Help

- **Documentation**: Read [INSTALLATION.md](docs/INSTALLATION.md) for detailed guide
- **Issues**: Report bugs on GitHub Issues
- **Discord**: Join our community (link in README)
- **Email**: <support@aisuperstudio.com>

## Quick Reference

| Component | URL | Purpose |
|-----------|-----|---------|
| Frontend | <http://localhost:5173> | Web interface |
| Backend | <http://localhost:5000> | API server |
| Health Check | <http://localhost:5000/api/health> | Verify backend is running |

| Mode | Description | Requires |
|------|-------------|----------|
| Online | Commercial APIs | ElevenLabs API key + Internet |
| Sandbox | Open-source models | Model downloads (no API key) |

## Development Mode

If you're a developer:

- Frontend runs with Hot Module Replacement (HMR)
- Backend runs with debug mode enabled
- Changes auto-reload in development

## Production Deployment

For production deployment:

```bash
# Frontend
cd frontend
npm run build
# Serve the dist/ folder

# Backend
# Set DEBUG=False in .env
# Use gunicorn or similar WSGI server
```

---

**🎉 You're all set! Enjoy creating with AI Super Studio!**

For a complete feature list, see the main [README.md](README.md)
