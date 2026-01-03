from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from services.voice_service import VoiceService
from services.video_service import VideoService
from services.model_manager import ModelManager
from services.agent_service import agent_service

load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize services
voice_service = VoiceService()
video_service = VideoService()
model_manager = ModelManager()
# agent_service is already instantiated in its module


# Configuration
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500MB max file size
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'outputs'

# Ensure directories exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

# ============================================================================
# VOICE ENDPOINTS
# ============================================================================


@app.route('/api/voice/generate', methods=['POST'])
def generate_speech():
    """Generate speech from text"""
    try:
        data = request.json
        text = data.get('text')
        voice = data.get('voice')
        model = data.get('model', 'eleven_multilingual_v2')
        api_key = request.headers.get('X-API-Key')

        if not text:
            return jsonify({'error': 'Text is required'}), 400

        # Determine mode based on model
        mode = 'sandbox' if model in [
            'coqui_xtts', 'piper', 'bark'
        ] else 'online'

        result = voice_service.generate_speech(
            text, voice, model, api_key, mode
        )
        return jsonify(result)


    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/voice/list', methods=['GET'])
def list_voices():
    """Get available voices"""
    try:
        api_key = request.headers.get('X-API-Key')
        voices = voice_service.get_voices(api_key)
        return jsonify(voices)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/voice/clone', methods=['POST'])
def clone_voice():
    """Clone a voice from audio samples"""
    try:
        files = request.files
        api_key = request.headers.get('X-API-Key')


        audio_files = []
        for key in files:
            if key.startswith('sample_'):
                audio_files.append(files[key])


        if len(audio_files) < 2:
            return jsonify({'error': 'At least 2 audio samples required'}), 400

        result = voice_service.clone_voice(audio_files, api_key)
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ============================================================================
# VIDEO ENDPOINTS
# ============================================================================


@app.route('/api/video/generate', methods=['POST'])
def generate_video():
    """Generate AI avatar video"""
    try:
        data = request.form
        script = data.get('script')
        avatar_style = data.get('avatar_style')
        
        if not script:
            return jsonify({'error': 'Script is required'}), 400
        
        result = video_service.generate_avatar_video(script, avatar_style)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/video/talking-photo', methods=['POST'])
def generate_talking_photo():
    """Generate talking photo from image and audio/text"""
    try:
        if 'photo' not in request.files:
            return jsonify({'error': 'Photo file required'}), 400
        
        photo = request.files['photo']
        text = request.form.get('text')
        audio = request.files.get('audio')
        
        result = video_service.generate_talking_photo(photo, text, audio)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/video/multi-avatar', methods=['POST'])
def generate_multi_avatar():
    """Generate multi-avatar conversation"""
    try:
        data = request.json
        script = data.get('script')
        
        if not script:
            return jsonify({'error': 'Script is required'}), 400
        
        result = video_service.generate_multi_avatar(script)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/video/style-transfer', methods=['POST'])
def apply_style_transfer():
    """Apply style transfer to video"""
    try:
        data = request.json
        video_id = data.get('videoId')
        style = data.get('style')
        
        result = video_service.apply_style_transfer(video_id, style)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ============================================================================
# MODEL MANAGEMENT ENDPOINTS
# ============================================================================


@app.route('/api/models/available', methods=['GET'])
def get_available_models():
    """Get list of available models for download"""
    try:
        models = model_manager.get_available_models()
        return jsonify(models)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/models/installed', methods=['GET'])
def get_installed_models():
    """Get list of installed models"""
    try:
        models = model_manager.get_installed_models()
        return jsonify(models)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/models/download', methods=['POST'])
def download_model():
    """Download a model"""
    try:
        data = request.json
        model_id = data.get('modelId')
        
        if not model_id:
            return jsonify({'error': 'Model ID required'}), 400
        
        job_id = model_manager.download_model(model_id)
        return jsonify({'jobId': job_id})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/models/<model_id>', methods=['DELETE'])
def delete_model(model_id):
    """Delete an installed model"""
    try:
        result = model_manager.delete_model(model_id)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/models/download-status/<job_id>', methods=['GET'])
def get_download_status(job_id):
    """Check model download status"""
    try:
        status = model_manager.get_download_status(job_id)
        return jsonify(status)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ============================================================================
# TRANSLATION ENDPOINTS
# ============================================================================


@app.route('/api/translation/global', methods=['POST'])
def translate_video():
    """Translate video to multiple languages"""
    try:
        data = request.json
        # video_id = data.get('videoId')
        target_languages = data.get('targetLanguages', [])
        
        # Placeholder for global translation
        return jsonify({
            'jobId': 'trans_' + os.urandom(8).hex(),
            'languages': target_languages,
            'status': 'processing'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/translation/accent', methods=['POST'])
def transform_accent():
    """Transform audio to different accent"""
    try:
        data = request.json
        # audio_id = data.get('audioId')
        target_accent = data.get('targetAccent')
        
        # Placeholder for accent transformation
        return jsonify({
            'jobId': 'accent_' + os.urandom(8).hex(),
            'accent': target_accent,
            'status': 'processing'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ============================================================================
# CONVERSATIONAL AI ENDPOINTS
# ============================================================================


@app.route('/api/conversational/agent/create', methods=['POST'])
def create_agent():
    """Create a new conversational AI agent"""
    try:
        data = request.json
        name = data.get('name', 'New Agent')
        prompt = data.get('system_prompt', 'You are a helpful assistant.')
        voice = data.get('voice_id', 'rachel')
        
        result = agent_service.create_agent(name, prompt, voice)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/conversational/agent/test', methods=['POST'])
def test_agent():
    """Test agent with a message"""
    try:
        data = request.json
        agent_id = data.get('agentId')
        message = data.get('message')
        
        if not agent_id or not message:
            return jsonify({'error': 'Missing agentId or message'}), 400
             
        result = agent_service.chat(agent_id, message)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ============================================================================
# HEALTH CHECK
# ============================================================================


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'version': '1.0.0',
        'services': {
            'voice': 'ready',
            'video': 'ready',
            'models': 'ready'
        }
    })

# ============================================================================
# ERROR HANDLERS
# ============================================================================


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'True') == 'True'
    app.run(host='0.0.0.0', port=port, debug=debug)
