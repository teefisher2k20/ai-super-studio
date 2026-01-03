# AI Super Studio - Quick Demo Setup Script
# This script helps you configure and test the application

import os

import webbrowser
import time


def print_header(text):
    print("\n" + "=" * 70)
    print(f"  {text}")
    print("=" * 70)


def check_env_file():
    """Check if .env file exists and has API key"""
    env_path = '.env'
    if not os.path.exists(env_path):
        print("❌ .env file not found!")
        return False

    with open(env_path, 'r') as f:
        content = f.read()
        if 'ELEVENLABS_API_KEY=' in content:
            # Check if it has a value
            for line in content.split('\n'):
                if line.startswith('ELEVENLABS_API_KEY='):
                    value = line.split('=', 1)[1].strip()
                    if value and value != 'your_api_key_here':
                        print("✅ ElevenLabs API key configured")
                        return True
    
    print("⚠️  ElevenLabs API key not configured")
    return False


def configure_api_key():
    """Help user configure API key"""
    print_header("API Key Configuration")
    print("\n📝 To use online mode, you need an ElevenLabs API key")
    print("   1. Visit: https://elevenlabs.io/app/settings/api-keys")
    print("   2. Create a free account (10,000 chars/month free)")
    print("   3. Click 'Create New Key' and copy it")
    
    response = input("\n   Open ElevenLabs website now? (y/n): ")
    if response.lower() == 'y':
        webbrowser.open('https://elevenlabs.io/app/settings/api-keys')
        print("   🌐 Opening browser...")
        time.sleep(2)
    
    print("\n   Once you have your API key:")
    api_key = input("   Paste it here (or press Enter to skip): ").strip()
    
    if api_key:
        # Update .env file
        env_path = '.env'
        if os.path.exists(env_path):
            with open(env_path, 'r') as f:
                content = f.read()
            
            # Replace the API key line
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if line.startswith('ELEVENLABS_API_KEY='):
                    lines[i] = f'ELEVENLABS_API_KEY={api_key}'
                    break
            
            with open(env_path, 'w') as f:
                f.write('\n'.join(lines))
            
            print("   ✅ API key saved to .env file!")
            return True
    
    print("   ⏭️  Skipped. You can add it later in Settings.")
    return False


def test_voice_generation():
    """Provide instructions for testing voice generation"""
    print_header("Test Voice Generation")
    print("\n🎤 Let's test the voice generation feature!")
    print("\n   Steps:")
    print("   1. The app will open in your browser")
    print("   2. Click 'Voice Studio' in the navigation")
    print("   3. Enter text: 'Hello! This is my first AI-generated speech.'")
    print("   4. Select voice: 'Rachel'")
    print("   5. Click 'Generate Speech'")
    print("   6. Listen to the result!")
    
    input("\n   Press Enter when ready to open the app...")
    webbrowser.open('http://localhost:5173/voice-studio')
    print("   🌐 Opening Voice Studio...")


def test_video_generation():
    """Provide instructions for testing video generation"""
    print_header("Test Video Generation")
    print("\n🎬 Video generation requires model checkpoints")
    print("\n   To enable video features:")
    print("   1. Run: python download_checkpoints.py")
    print("   2. Download Wav2Lip checkpoint (~400 MB)")
    print("   3. Go to Video Studio in the app")
    print("   4. Upload a photo and audio file")
    print("   5. Generate talking photo!")
    
    response = input("\n   Download checkpoints now? (y/n): ")
    if response.lower() == 'y':
        print("\n   Run this command:")
        print("   python download_checkpoints.py")


def main():
    print_header("AI Super Studio - Quick Demo Setup")
    print("\n🚀 Welcome! This script will help you set up and test the app.")
    
    # Check if servers are running
    print("\n📡 Checking if servers are running...")
    print("   Frontend should be at: http://localhost:5173")
    print("   Backend should be at: http://localhost:5000")
    print("\n   If not running, execute: start.bat (or start.sh)")
    
    input("\n   Press Enter to continue...")
    
    # Check API key
    has_api_key = check_env_file()
    
    if not has_api_key:
        response = input("\n   Configure API key now? (y/n): ")
        if response.lower() == 'y':
            configure_api_key()
    
    # Main menu
    while True:
        print_header("Demo Options")
        print("\n1. Test Voice Generation (Online Mode)")
        print("2. Test Video Generation (Requires Checkpoints)")
        print("3. Configure API Key")
        print("4. Download Model Checkpoints")
        print("5. Open Dashboard")
        print("6. View Documentation")
        print("7. Exit")
        
        choice = input("\nEnter choice (1-7): ").strip()
        
        if choice == '1':
            test_voice_generation()
        elif choice == '2':
            test_video_generation()
        elif choice == '3':
            configure_api_key()
        elif choice == '4':
            print("\n   Run: python download_checkpoints.py")
        elif choice == '5':
            webbrowser.open('http://localhost:5173')
            print("   🌐 Opening dashboard...")
        elif choice == '6':
            print("\n   📚 Documentation files:")
            print("   - README.md - Project overview")
            print("   - SETUP_GUIDE.md - Setup instructions")
            print("   - docs/FEATURES.md - Feature specifications")
            print("   - docs/INSTALLATION.md - Installation guide")
        elif choice == '7':
            print("\n👋 Goodbye! Enjoy creating with AI Super Studio!")
            break
        else:
            print("   ❌ Invalid choice")


if __name__ == "__main__":
    # Change to backend directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    main()
