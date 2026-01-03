# AI Super Studio - Complete Setup Guide

## ✅ Current Status (2026-01-01)

### What's Working

- ✅ Frontend running on <http://localhost:5173>
- ✅ Backend running on <http://localhost:5000>
- ✅ ElevenLabs integration ready
- ✅ Wav2Lip repository cloned
- ✅ SadTalker repository cloned

### What Needs Setup

- ⚠️ Coqui TTS (requires C++ Build Tools)
- ⚠️ Model checkpoint weights
- ⚠️ ElevenLabs API key configuration

---

## 🔧 Step-by-Step Setup

### Option 1: Quick Start (Online Mode Only)

**Best for**: Testing the app immediately with commercial APIs

1. **Get ElevenLabs API Key**
   - Visit: <https://elevenlabs.io/app/settings/api-keys>
   - Create a free account (10,000 characters/month free)
   - Click "Create New Key" and copy it

2. **Configure API Key**

   ```bash
   # Edit backend/.env file
   ELEVENLABS_API_KEY=your_key_here
   ```

3. **Test Voice Generation**
   - Open <http://localhost:5173>
   - Go to Voice Studio
   - Enter text and click "Generate Speech"

### Option 2: Full Offline Setup (Sandbox Mode)

**Best for**: Running 100% offline with open-source models

#### A. Fix Coqui TTS Installation

**Method 1: Install Visual C++ Build Tools** (Recommended)

```bash
# Download and install from:
# https://visualstudio.microsoft.com/visual-cpp-build-tools/
# Then retry:
cd backend
./venv/Scripts/pip.exe install TTS
```

**Method 2: Use Alternative TTS** (Skip Coqui)

- The app will work with ElevenLabs in online mode
- Or use Piper TTS (lighter, no compilation needed)

#### B. Download Model Checkpoints

**Wav2Lip Weights** (Required for talking photos)

```bash
# Download from:
# https://github.com/Rudrabha/Wav2Lip#getting-the-weights

# Place in:
# backend/models/wav2lip/checkpoints/wav2lip_gan.pth
```

**SadTalker Weights** (Required for advanced avatars)

```bash
# Download from:
# https://github.com/OpenTalker/SadTalker#1-installation

# Follow their checkpoint download instructions
```

---

## 🎯 Quick Test Scenarios

### Test 1: Voice Generation (Online)

1. Add ElevenLabs API key to `backend/.env`
2. Restart backend: `./venv/Scripts/python.exe app.py`
3. Open <http://localhost:5173/voice-studio>
4. Enter text: "Hello! This is my first AI-generated speech."
5. Select voice: "Rachel"
6. Click "Generate Speech"

### Test 2: Model Management

1. Open <http://localhost:5173/settings>
2. Scroll to "Model Management"
3. Click "Download" on any model
4. Check download progress

### Test 3: Multi-Avatar Conversation

1. Go to <http://localhost:5173/multi-avatar>
2. Enter script:

   ```
   ALICE: Hello, how are you today?
   BOB: I'm doing great, thanks for asking!
   ALICE: That's wonderful to hear!
   ```

3. Click "Generate Conversation"

---

## 📦 Model Download Links

### Voice Models

- **Coqui XTTS-v2**: Auto-downloads on first use (if installed)
- **Piper TTS**: <https://github.com/rhasspy/piper/releases>

### Video Models

- **Wav2Lip Checkpoint**:
  - GAN Model: <https://iiitaphyd-my.sharepoint.com/:u:/g/personal/radrabha_m_research_iiit_ac_in/EdjI7bZlgApMqsVoEUUXpLsBxqXbn5z8VTmoxp55YNDcIA?e=n9ljGW>
  - Regular Model: <https://iiitaphyd-my.sharepoint.com/:u:/g/personal/radrabha_m_research_iiit_ac_in/Eb3LEzbfuKlJiR600lQWRxgBIY27JZdQ7g4QbJQQkT_Zsg?e=TBFBVW>

- **SadTalker Checkpoints**:
  - Follow: <https://github.com/OpenTalker/SadTalker/blob/main/docs/install.md#download-models>

- **GFPGAN** (Face Enhancement):
  - Auto-downloads when needed

---

## 🐛 Troubleshooting

### Issue: "TTS installation failed"

**Solution**:

- Skip Coqui TTS and use online mode
- Or install Visual C++ Build Tools
- Or use Piper TTS instead

### Issue: "API key not working"

**Solution**:

- Check for extra spaces in .env file
- Verify key is valid on ElevenLabs dashboard
- Restart backend server after changing .env

### Issue: "Wav2Lip model not found"

**Solution**:

- Download checkpoint weights (see links above)
- Place in `backend/models/wav2lip/checkpoints/`
- Ensure filename is exactly `wav2lip_gan.pth` or `wav2lip.pth`

### Issue: "Port already in use"

**Solution**:

```bash
# Change backend port in backend/.env
PORT=5001

# Frontend will auto-select next available port
```

---

## 🚀 Next Steps

1. **Configure API Key** → Test voice generation
2. **Download Checkpoints** → Enable video features
3. **Explore Features** → Try all 6 studio pages
4. **Read Documentation** → Check FEATURES.md for all 40+ features

---

## 📚 Additional Resources

- **Main README**: `README.md`
- **Feature Specs**: `docs/FEATURES.md`
- **Installation Guide**: `docs/INSTALLATION.md`
- **Project Overview**: `PROJECT_OVERVIEW.md`

**Need Help?** Check the troubleshooting section or review the documentation files.
