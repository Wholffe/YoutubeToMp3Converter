import yt_dlp
import os
from pathlib import Path

class Downloader():
    def __init__(self):
        self.download_path = str(Path.home() / "Downloads/ytdownloader")
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
            'progress_hooks': [self.progress_hook],
            'noplaylist': True,
        }
        self.current_download_url = ''

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            percent = d.get('percent', 0)
            self.status_callback(percent)

        elif d['status'] == 'finished':
            self.status_callback(100, "Download completed")

        elif d['status'] == 'error':
            error_message = d.get('error', 'Unknown error')
            self.status_callback(None, error_message)

    def download(self, url, path, status_callback):
        self.status_callback = status_callback
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                self.status_callback(10)
                self.current_download_url = url
                info_dict = ydl.extract_info(url, download=False)
                video_title = info_dict.get('title', 'Unknown Title')
                self.status_callback(20)  
                self.status_callback(None, f"'{video_title}' has been saved to '{self.download_path}'.")
                ydl.download([url])
        except Exception as e:
            self.status_callback(None, f"Error: {str(e)}")