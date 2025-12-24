@echo off
echo ========================================
echo AI Super Studio - Setup Script
echo ========================================
echo.

echo [1/5] Setting up backend...
cd backend

echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing Python dependencies...
pip install --upgrade pip
pip install -r requirements.txt

echo Creating .env file...
if not exist .env copy .env.example .env

echo.
echo [2/5] Creating necessary directories...
if not exist uploads mkdir uploads
if not exist outputs mkdir outputs
if not exist outputs\audio mkdir outputs\audio
if not exist outputs\video mkdir outputs\video
if not exist models mkdir models

cd ..

echo.
echo [3/5] Setting up frontend...
cd frontend

echo Installing Node.js dependencies...
call npm install

cd ..

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Edit backend\.env and add your ElevenLabs API key
echo 2. Run start.bat to start both servers
echo.
echo For more info, see docs\INSTALLATION.md
echo.
pause
