import os
import json
import threading
import time
from utils.downloader import Downloader


class ModelManager:
    """Service for managing open-source models"""
    
    def __init__(self):
        self.models_dir = 'models'
        self.downloads_file = 'models/downloads.json'
        # Ensure absolute path for robustness
        if not os.path.isabs(self.models_dir):
            self.models_dir = os.path.join(os.getcwd(), self.models_dir)
            
        os.makedirs(self.models_dir, exist_ok=True)
        
        # Initialize downloads tracking
        if not os.path.exists(self.downloads_file):
            with open(self.downloads_file, 'w') as f:
                json.dump({}, f)

    def get_available_models(self):
        """Get list of available models for download"""
        return {
            'models': [
                {
                    'id': 'wav2lip',
                    'name': 'Wav2Lip',
                    'type': 'video',
                    'description': 'Accurate lip-sync key model',
                    'size': '~400 MB',
                    'source': 'https://github.com/Rudrabha/Wav2Lip'
                },
                {
                    'id': 'sadtalker',
                    'name': 'SadTalker',
                    'type': 'video',
                    'description': 'Talking photo generation',
                    'size': '~500 MB',
                    'source': 'https://github.com/OpenTalker/SadTalker'
                },
                {
                    'id': 'gfpgan',
                    'name': 'GFPGAN',
                    'type': 'video',
                    'description': 'Face enhancer (required for quality)',
                    'size': '300 MB',
                    'source': 'https://github.com/TencentARC/GFPGAN'
                }
            ]
        }

    def get_installed_models(self):
        """Get list of installed models"""
        installed = []
        if os.path.exists(self.models_dir):
            for item in os.listdir(self.models_dir):
                item_path = os.path.join(self.models_dir, item)
                if os.path.isdir(item_path) and not item.startswith('.'):
                    installed.append({
                        'id': item,
                        'name': item.title(),
                        'status': 'installed',
                        'path': item_path
                    })
        return {'models': installed}

    def download_model(self, model_id):
        """Start a background download job"""
        job_id = f"job_{int(time.time())}"
        
        # Initialize job status
        self._update_job_status(job_id, model_id, 'pending', 0)
        
        # Start background thread
        thread = threading.Thread(
            target=self._perform_download,
            args=(job_id, model_id)
        )
        thread.daemon = True
        thread.start()
        
        return job_id

    def _perform_download(self, job_id, model_id):
        """Actual download logic running in thread"""
        try:
            self._update_job_status(job_id, model_id, 'downloading', 10)
            target_dir = os.path.join(self.models_dir, model_id)
            
            success = False
            
            # Update progress wrapper
            def update_progress(p):
                self._update_job_status(job_id, model_id, 'downloading', p)

            if model_id == 'wav2lip':
                update_progress(20)
                # 1. Clone Repo
                if Downloader.git_clone(
                    "https://github.com/Rudrabha/Wav2Lip.git", target_dir
                ):
                    update_progress(50)
                    # 2. Download Model Weights (Wav2Lip + GAN) using a public mirror or placeholder
                    # Note: Original GDrive links often require auth, using a placeholder check for now
                    # Users usually have to download these manually or we provide a direct link mirror
                    print(
                        "Wav2Lip repo cloned. Note: Weights require manual download or direct link."
                    )
                    success = True
                    
            elif model_id == 'sadtalker':
                update_progress(20)
                if Downloader.git_clone(
                    "https://github.com/OpenTalker/SadTalker.git", target_dir
                ):
                    success = True
            
            elif model_id == 'gfpgan':
                update_progress(20)
                if Downloader.git_clone(
                    "https://github.com/TencentARC/GFPGAN.git", target_dir
                ):
                    success = True
            
            else:
                # Generic Repo Clone for unknown models
                # Attempt to find source from available models
                avail = self.get_available_models()['models']
                source = next(
                    (m['source'] for m in avail if m['id'] == model_id), None
                )
                if source:
                    if Downloader.git_clone(source, target_dir):
                        success = True

            if success:
                self._update_job_status(job_id, model_id, 'completed', 100)
            else:
                self._update_job_status(
                    job_id, model_id, 'failed', 0, "Download failed"
                )

        except Exception as e:
            print(f"Download thread error: {e}")
            self._update_job_status(job_id, model_id, 'failed', 0, str(e))

    def _update_job_status(
        self, job_id, model_id, status, progress, error=None
    ):
        """Helper to update JSON status file"""
        try:
            data = {}
            if os.path.exists(self.downloads_file):
                try:
                    with open(self.downloads_file, 'r') as f:
                        data = json.load(f)
                except Exception:
                    pass
            
            data[job_id] = {
                'modelId': model_id,
                'status': status,
                'progress': progress,
                'error': error,
                'timestamp': time.time()
            }
            
            with open(self.downloads_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error updating job status: {e}")

    def get_download_status(self, job_id):
        """Get status of a specific job"""
        if os.path.exists(self.downloads_file):
            with open(self.downloads_file, 'r') as f:
                data = json.load(f)
                return data.get(job_id, {'status': 'unknown'})
        return {'status': 'unknown'}

    def delete_model(self, model_id):
        """Delete an installed model"""
        import shutil
        target_path = os.path.join(self.models_dir, model_id)
        if os.path.exists(target_path):
            shutil.rmtree(target_path)
            # Cleanup downloads file? Maybe not needed
            return {'status': 'deleted'}
        return {'error': 'Model not found'}
