import os
import subprocess
import shutil

class VideoService:
    """Service for video generation and processing"""
    
    def __init__(self):
        self.output_dir = 'outputs/video'
        self.models_dir = 'models'
        os.makedirs(self.output_dir, exist_ok=True)
    
    def generate_avatar_video(self, script, avatar_style):
        """Generate AI avatar video from script"""
        # In a real offline implementation, this would:
        # 1. Generate audio from script (using VoiceService)
        # 2. Use SadTalker or Wav2Lip to animate a face
        
        # For now, we return a mock response but ready to hook into Wav2Lip
        filename = f"avatar_{os.urandom(8).hex()}.mp4"
        return {
            'videoUrl': f'/outputs/video/{filename}',
            'status': 'mock_success',
            'note': 'Full pipeline requires connecting VoiceService audio -> Wav2Lip'
        }
    
    def generate_talking_photo(self, photo, text, audio):
        """Generate talking photo using Wav2Lip"""
        try:
            # 1. Save inputs
            photo_filename = f"input_{os.urandom(8).hex()}.jpg"
            photo_path = os.path.join('uploads', photo_filename)
            photo.save(photo_path)
            
            # If audio file provided, save it. If text, generate audio first (skip for now)
            if audio:
                audio_filename = f"input_{os.urandom(8).hex()}.wav"
                audio_path = os.path.join('uploads', audio_filename)
                audio.save(audio_path)
            else:
                # TODO: Call VoiceService to generate audio from 'text'
                return {'error': 'Text-to-audio for video not yet connected. Please upload audio file.'}

            # 2. Prepare paths
            wav2lip_dir = os.path.join(self.models_dir, 'wav2lip')
            output_filename = f"talking_{os.urandom(8).hex()}.mp4"
            output_path = os.path.join(self.output_dir, output_filename)
            
            # Check if Wav2Lip model exists (the checkpoint)
            checkpoint_path = os.path.join(wav2lip_dir, 'checkpoints', 'wav2lip_gan.pth')
            # Fallback to standard model if GAN not found
            if not os.path.exists(checkpoint_path):
                 checkpoint_path = os.path.join(wav2lip_dir, 'checkpoints', 'wav2lip.pth')
            
            if not os.path.exists(checkpoint_path):
                return {
                    'error': 'Wav2Lip model weights not found. Please download wav2lip.pth to backend/models/wav2lip/checkpoints/'
                }

            # 3. Construct command
            # python inference.py --checkpoint_path <ckpt> --face <img/video> --audio <audio> --outfile <out>
            
            # Ensure we use the python env that has wav2lip requirements
            # Assuming current env has them or we use a specific one
            python_exe = sys.executable
            
            cmd = [
                python_exe,
                os.path.join(wav2lip_dir, 'inference.py'),
                '--checkpoint_path', checkpoint_path,
                '--face', photo_path,
                '--audio', audio_path,
                '--outfile', output_path,
                # '--resize_factor', '2' # Optional: reduce resolution for speed
            ]
            
            print(f"Running Wav2Lip: {' '.join(cmd)}")
            
            # 4. Run Inference
            # Note: inference.py needs to be run with CWD as wav2lip_dir usually, 
            # or we ensure imports working. Safest is to set cwd.
            process = subprocess.Popen(
                cmd,
                cwd=wav2lip_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            stdout, stderr = process.communicate()
            
            if process.returncode != 0:
                print(f"Wav2Lip Error: {stderr.decode()}")
                return {'error': 'Wav2Lip inference failed', 'details': stderr.decode()}

            return {
                'videoUrl': f'/outputs/video/{output_filename}',
                'duration': 0,
                'format': 'mp4',
                'status': 'completed'
            }

        except Exception as e:
            print(f"Generate talking photo error: {e}")
            return {'error': str(e)}

    def generate_multi_avatar(self, script):
        """Generate multi-avatar conversation"""
        filename = f"multi_avatar_{os.urandom(8).hex()}.mp4"
        return {
            'videoUrl': f'/outputs/video/{filename}',
            'status': 'processing',
            'note': 'Multi-avatar generation - integration in progress'
        }
    
    def apply_style_transfer(self, video_id, style):
        filename = f"styled_{os.urandom(8).hex()}.mp4"
        return {
            'videoUrl': f'/outputs/video/{filename}',
            'style': style,
            'status': 'processing'
        }
