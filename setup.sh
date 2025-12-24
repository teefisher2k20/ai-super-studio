#!/bin/bash

echo "========================================"
echo "AI Super Studio - Setup Script"
echo "========================================"
echo ""

echo "[1/5] Setting up backend..."
cd backend

echo "Creating virtual environment..."
python3 -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Creating .env file..."
if [ ! -f .env ]; then
    cp .env.example .env
fi

echo ""
echo "[2/5] Creating necessary directories..."
mkdir -p uploads
mkdir -p outputs/audio
mkdir -p outputs/video
mkdir -p models

cd ..

echo ""
echo "[3/5] Setting up frontend..."
cd frontend

echo "Installing Node.js dependencies..."
npm install

cd ..

echo ""
echo "========================================"
echo "Setup Complete!"
echo "========================================"
echo ""
echo "Next steps:"
echo "1. Edit backend/.env and add your ElevenLabs API key"
echo "2. Run ./start.sh to start both servers"
echo ""
echo "For more info, see docs/INSTALLATION.md"
echo ""
