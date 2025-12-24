import os
import sys
import time
import subprocess

# Add backend directory to path so we can import utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.downloader import Downloader

MODELS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models')

def print_header():
    print("="*60)
    print("AI Super Studio - Model Downloader")
    print("="*60)
    print(f"Target Directory: {MODELS_DIR}")
    print("="*60)

def download_wav2lip():
    print("\n[1/3] Setting up Wav2Lip...")
    target = os.path.join(MODELS_DIR, 'wav2lip')
    
    if not os.path.exists(target):
        print("Cloning repository...")
        if Downloader.git_clone("https://github.com/Rudrabha/Wav2Lip.git", target):
            print("✅ Repository cloned")
            
            # Relax requirements to avoid conflicts
            req_file = os.path.join(target, "requirements.txt")
            if os.path.exists(req_file):
                with open(req_file, 'r') as f:
                    content = f.read()
                
                # Remove specific version constraints that cause conflicts
                content = content.replace('==', '>=')
                content = content.replace('librosa>=0.7.0', 'librosa')
                content = content.replace('numpy>=1.17', 'numpy')
                
                with open(req_file, 'w') as f:
                    f.write(content)
            
            print("Installing requirements (this may take a moment)...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", req_file])
                print("✅ Requirements installed")
            except subprocess.CalledProcessError:
                 print("⚠️ Warning: Some requirements failed to install. You may need to install them manually.")

            
        else:
            print("❌ Failed to clone repository")
    else:
        print("✅ Wav2Lip already exists")

def download_sadtalker():
    print("\n[2/3] Setting up SadTalker...")
    target = os.path.join(MODELS_DIR, 'sadtalker')
    
    if not os.path.exists(target):
        print("Cloning repository...")
        if Downloader.git_clone("https://github.com/OpenTalker/SadTalker.git", target):
            print("✅ Repository cloned")
            
            # Note: SadTalker requirements are heavy, we skip auto-install to avoid conflicts
            print("ℹ️  Note: SadTalker requires additional valid checkpoint downloads.")
            print("    Please check backend/models/sadtalker/README.md for weight links.")
        else:
            print("❌ Failed to clone repository")
    else:
        print("✅ SadTalker already exists")

def download_coqui():
    print("\n[3/3] Setting up Coqui TTS...")
    # Coqui is a package, but we can download models
    try:
        import TTS
        print("✅ Coqui TTS package found")
    except ImportError:
        print("Installing Coqui TTS package...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "TTS"])
        print("✅ Coqui TTS installed")

def main():
    print_header()
    
    os.makedirs(MODELS_DIR, exist_ok=True)
    
    import subprocess
    
    # Check for git
    try:
        subprocess.check_call(['git', '--version'], stdout=subprocess.DEVNULL)
    except:
        print("❌ Error: Git is not installed or not in PATH.")
        print("Please install Git to continue.")
        return

    while True:
        print("\nAvailable Actions:")
        print("1. Download All Core Models (Wav2Lip, SadTalker, Coqui)")
        print("2. Download Wav2Lip only")
        print("3. Download SadTalker only")
        print("4. Exit")
        
        choice = input("\nEnter choice (1-4): ")
        
        if choice == '1':
            download_wav2lip()
            download_sadtalker()
            download_coqui()
            print("\n✅ All tasks completed!")
            break
        elif choice == '2':
            download_wav2lip()
            break
        elif choice == '3':
            download_sadtalker()
            break
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
