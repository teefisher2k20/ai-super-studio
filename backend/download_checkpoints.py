"""
Download Model Checkpoints for AI Super Studio

This script helps download the required model checkpoint files
for Wav2Lip, SadTalker, and other models.
"""

import os
import sys
import requests

from tqdm import tqdm

# Model checkpoint URLs
CHECKPOINTS = {
    'wav2lip_gan': {
        'url': (
            'https://iiitaphyd-my.sharepoint.com/:u:/g/personal/'
            'radrabha_m_research_iiit_ac_in/'
            'EdjI7bZlgApMqsVoEUUXpLsBxqXbn5z8VTmoxp55YNDcIA?e=n9ljGW&download=1'
        ),
        'path': 'models/wav2lip/checkpoints/wav2lip_gan.pth',
        'size': '~400 MB',
        'description': 'Wav2Lip GAN model (best quality)'
    },
    'wav2lip': {
        'url': (
            'https://iiitaphyd-my.sharepoint.com/:u:/g/personal/'
            'radrabha_m_research_iiit_ac_in/'
            'Eb3LEzbfuKlJiR600lQWRxgBIY27JZdQ7g4QbJQQkT_Zsg?e=TBFBVW&download=1'
        ),
        'path': 'models/wav2lip/checkpoints/wav2lip.pth',
        'size': '~350 MB',
        'description': 'Wav2Lip standard model'
    },
}




def download_file(url, destination, description="Downloading"):
    """Download a file with progress bar"""
    try:
        print(f"\n📥 {description}")
        print(f"   URL: {url[:60]}...")
        print(f"   Destination: {destination}")


        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(destination), exist_ok=True)


        # Check if file already exists
        if os.path.exists(destination):
            response = input("   File already exists. Overwrite? (y/n): ")
            if response.lower() != 'y':
                print("   ⏭️  Skipped")
                return True


        # Download with progress bar
        response = requests.get(url, stream=True, allow_redirects=True)
        response.raise_for_status()


        total_size = int(response.headers.get('content-length', 0))


        with open(destination, 'wb') as f, tqdm(
            desc="   Progress",
            total=total_size,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
        ) as pbar:
            for chunk in response.iter_content(chunk_size=8192):
                size = f.write(chunk)
                pbar.update(size)


        print("   ✅ Downloaded successfully!")
        return True


    except Exception as e:
        print(f"   ❌ Error: {str(e)}")
        return False


def main():
    print("=" * 70)
    print("AI Super Studio - Checkpoint Downloader")
    print("=" * 70)
    print("\nThis script will download model checkpoints for:")
    print("  • Wav2Lip (lip-sync video generation)")
    print("  • SadTalker (talking photo animation)")
    print("\n⚠️  Note: Downloads may be large (300-500 MB each)")
    print("=" * 70)


    while True:
        print("\nAvailable Downloads:")
        print("1. Wav2Lip GAN Model (~400 MB) - Best quality")
        print("2. Wav2Lip Standard Model (~350 MB) - Good quality")
        print("3. Download All")
        print("4. Manual Download Instructions")
        print("5. Exit")


        choice = input("\nEnter choice (1-5): ").strip()


        if choice == '1':
            download_file(
                CHECKPOINTS['wav2lip_gan']['url'],
                CHECKPOINTS['wav2lip_gan']['path'],
                CHECKPOINTS['wav2lip_gan']['description']
            )
        elif choice == '2':
            download_file(
                CHECKPOINTS['wav2lip']['url'],
                CHECKPOINTS['wav2lip']['path'],
                CHECKPOINTS['wav2lip']['description']
            )
        elif choice == '3':
            for key, checkpoint in CHECKPOINTS.items():
                download_file(
                    checkpoint['url'],
                    checkpoint['path'],
                    checkpoint['description']
                )
        elif choice == '4':
            print("\n" + "=" * 70)
            print("MANUAL DOWNLOAD INSTRUCTIONS")
            print("=" * 70)
            print("\n📦 Wav2Lip Checkpoints:")

            print("   1. Visit: https://github.com/Rudrabha/Wav2Lip#getting-the-weights")
            print("   2. Download wav2lip_gan.pth or wav2lip.pth")
            print("   3. Place in: backend/models/wav2lip/checkpoints/")


            print("\n📦 SadTalker Checkpoints:")
            print("   1. Visit: https://github.com/OpenTalker/SadTalker")
            print("   2. Follow their checkpoint download instructions")
            print("   3. Place in: backend/models/sadtalker/checkpoints/")


            print("\n📦 GFPGAN (Face Enhancement):")
            print("   Auto-downloads when needed")
            print("=" * 70)


        elif choice == '5':
            print("\n👋 Exiting...")
            break
        else:
            print("❌ Invalid choice. Please try again.")


    print("\n✅ Done! You can now use the models in AI Super Studio.")
    print("   Start the app with: start.bat (or start.sh on Linux/Mac)")


if __name__ == "__main__":
    try:
        import tqdm as _tqdm
        # silence unused warning
        _ = _tqdm
    except ImportError:
        print("Installing required package: tqdm")
        os.system(f"{sys.executable} -m pip install tqdm")
        from tqdm import tqdm


    main()
