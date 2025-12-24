import os
from elevenlabs.client import ElevenLabs

class VoiceService:
    """Service for voice generation and cloning"""
    
    def __init__(self):
        self.output_dir = 'outputs/audio'
        os.makedirs(self.output_dir, exist_ok=True)
    
    def generate_speech(self, text, voice, model, api_key, mode='online'):
        """Generate speech from text"""
        try:
            if mode == 'online':
                return self._generate_online(text, voice, model, api_key)
            else:
                return self._generate_sandbox(text, voice, model)
        except Exception as e:
            raise Exception(f"Speech generation failed: {str(e)}")
    
    def _generate_online(self, text, voice, model, api_key):
        """Generate using ElevenLabs API"""
        if not api_key:
            raise Exception("API key required for online mode")
        
        try:
            client = ElevenLabs(api_key=api_key)
            
            # Use default voice if not specified
            voice_id = self._get_voice_id(voice)
            
            audio = client.text_to_speech.convert(
                text=text,
                voice_id=voice_id,
                model_id=model,
                output_format="mp3_44100_128"
            )
            
            # Save audio file
            filename = f"speech_{os.urandom(8).hex()}.mp3"
            filepath = os.path.join(self.output_dir, filename)
            
            with open(filepath, 'wb') as f:
                for chunk in audio:
                    if isinstance(chunk, bytes):
                        f.write(chunk)
            
            return {
                'audioUrl': f'/outputs/audio/{filename}',
                'duration': 0,  # Calculate if needed
                'format': 'mp3'
            }
        
        except Exception as e:
            raise Exception(f"ElevenLabs API error: {str(e)}")
    
    def _generate_sandbox(self, text, voice, model):
        """Generate using open-source models (offline)"""
        filename = f"speech_{os.urandom(8).hex()}.wav"
        filepath = os.path.join(self.output_dir, filename)
        
        if model == 'coqui_xtts':
            try:
                from TTS.api import TTS
                import torch
                
                # Check if CUDA is available for faster generation
                device = "cuda" if torch.cuda.is_available() else "cpu"
                print(f"Using device: {device} for Coqui TTS")
                
                # Verify model is downloaded/cached
                # This will auto-download on first run if not present in default cache
                tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
                
                # Use a reference audio file for voice cloning if provided, 
                # otherwise use a default speaker from the model if available? 
                # XTTS v2 requires a speaker_wav for cloning.
                # For this implementation, we'll assume a default reference exists or use a provided one.
                # Ideally, 'voice' parameter should map to a file path in 'uploads' or 'models/voices'
                
                speaker_wav = self._get_sandbox_voice_path(voice)
                
                if not os.path.exists(speaker_wav):
                     # Fallback to a default sample if specific voice not found
                     # You might want to ship a default sample.wav
                     pass
                
                tts.tts_to_file(
                    text=text, 
                    speaker_wav=speaker_wav, 
                    language="en", 
                    file_path=filepath
                )
                
                return {
                    'audioUrl': f'/outputs/audio/{filename}',
                    'duration': 0, # Calculate if possible
                    'format': 'wav',
                    'note': f'Generated with Coqui XTTS on {device}'
                }
            except ImportError:
                 return {'error': 'TTS library not installed. Please run pip install TTS'}
            except Exception as e:
                print(f"Coqui TTS Error: {e}")
                raise Exception(f"Coqui generation failed: {str(e)}")
        
        elif model == 'piper':
            # Placeholder for Piper
            pass
            
        return {
            'audioUrl': f'/outputs/audio/{filename}',
            'note': 'Model not yet fully implemented'
        }

    def _get_sandbox_voice_path(self, voice_id):
        """Get path to speaker reference file for voice cloning"""
        # 1. Check if it's a cloned voice in uploads
        # 2. Check if it's a preset in models/voices
        # For now, return a dummy path or a real default one we create
        
        # Create a default reference if it doesn't exist for testing
        default_voice_dir = "models/voices"
        os.makedirs(default_voice_dir, exist_ok=True)
        default_voice_path = os.path.join(default_voice_dir, "default_speaker.wav")
        
        # If user selected a specific uploaded voice (logic to be added), map it here
        # For this demo, strictly return default if 'voice_id' doesn't match a file
        return default_voice_path
    
    def get_voices(self, api_key):
        """Get available voices"""
        try:
            if api_key:
                client = ElevenLabs(api_key=api_key)
                response = client.voices.get_all()
                return {'voices': [v.model_dump() for v in response.voices]}
            else:
                # Return default voices
                return {
                    'voices': [
                        {'voice_id': 'rachel', 'name': 'Rachel', 'category': 'premade'},
                        {'voice_id': 'george', 'name': 'George', 'category': 'premade'},
                        {'voice_id': 'bella', 'name': 'Bella', 'category': 'premade'},
                        {'voice_id': 'adam', 'name': 'Adam', 'category': 'premade'},
                    ]
                }
        except Exception as e:
            raise Exception(f"Failed to get voices: {str(e)}")
    
    def clone_voice(self, audio_files, api_key):
        """Clone voice from audio samples"""
        if not api_key:
            raise Exception("API key required for voice cloning")
        
        try:
            client = ElevenLabs(api_key=api_key)
            
            # Save uploaded files temporarily
            temp_files = []
            for i, file in enumerate(audio_files):
                temp_path = f'uploads/sample_{i}_{os.urandom(4).hex()}.mp3'
                file.save(temp_path)
                temp_files.append(temp_path)
            
            # Create voice clone
            voice_name = f"Clone_{os.urandom(4).hex()}"
            voice = client.voices.add(
                name=voice_name,
                description="Voice clone",
                files=temp_files
            )
            
            # Clean up temp files
            for temp_file in temp_files:
                if os.path.exists(temp_file):
                    os.remove(temp_file)
            
            return {
                'voiceId': voice.voice_id,
                'voiceName': voice_name,
                'status': 'created'
            }
        
        except Exception as e:
            raise Exception(f"Voice cloning failed: {str(e)}")
    
    def _get_voice_id(self, voice_name):
        """Map voice names to IDs"""
        voice_map = {
            'rachel': '21m00Tcm4TlvDq8ikWAM',
            'george': 'JBFqnCBsd6RMkjVDRZzb',
            'bella': 'EXAVITQu4vr4xnSDxMaL',
            'adam': 'pNInz6obpgDQGcFmaJgB'
        }
        return voice_map.get(voice_name, '21m00Tcm4TlvDq8ikWAM')  # Default to Rachel
