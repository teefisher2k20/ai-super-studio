import os
import requests
import subprocess


class Downloader:
    @staticmethod
    def download_file(url, target_path, progress_callback=None):
        """Download a file with progress tracking"""
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()

            total_size = int(response.headers.get('content-length', 0))
            block_size = 8192
            downloaded_size = 0
            os.makedirs(os.path.dirname(target_path), exist_ok=True)

            with open(target_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=block_size):
                    if chunk:
                        f.write(chunk)
                        downloaded_size += len(chunk)
                        if progress_callback and total_size > 0:
                            progress = int(
                                (downloaded_size / total_size) * 100
                            )
                            progress_callback(progress)

            if progress_callback:
                progress_callback(100)

            return True
        except Exception as e:
            print(f"Error downloading {url}: {e}")
            return False

    @staticmethod
    def git_clone(repo_url, target_dir, progress_callback=None):
        """Clone a git repository"""
        try:
            if os.path.exists(target_dir):
                print(
                    f"Directory {target_dir} already exists. Skipping clone."
                )
                if progress_callback:
                    progress_callback(100)
                return True

            # Create parent dir
            os.makedirs(os.path.dirname(target_dir), exist_ok=True)

            # Simple clone (subprocess blocks, so we fake progress for now
            # or just wait)
            if progress_callback:
                progress_callback(10)

            process = subprocess.Popen(
                ['git', 'clone', repo_url, target_dir],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            stdout, stderr = process.communicate()

            if process.returncode == 0:
                if progress_callback:
                    progress_callback(100)
                return True
            else:
                print(f"Git clone failed: {stderr.decode()}")
                return False

        except Exception as e:
            print(f"Error cloning {repo_url}: {e}")
            return False
