import yt_dlp
import os
from pathlib import Path

class Downloader():
    def __init__(self):
        self.download_path = str(Path.home() / "Downloads/ytdownloader")
        self.current_download_url = ''
        self.formats = {
            'mp3': {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferedformat': '192',
                }]
            },
            'mp4': {
                'format': 'bestvideo+bestaudio',
                'postprocessors': [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4',
                }]
            },
            'webm': {'format': 'bestvideo+bestaudio'}
        }

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            percent = d.get('percent', 0)
            self.status_callback(percent)
        elif d['status'] == 'finished':
            self.status_callback(100, "Download completed")
        elif d['status'] == 'error':
            error_message = d.get('error', 'Unknown error')
            self.status_callback(None, error_message)

    def download(self, url, file_format, status_callback):
        self.status_callback = status_callback
        self.current_download_url = url
        ydl_opts = self.getYDLOpts(file_format)
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                self.status_callback(10)
                info_dict = ydl.extract_info(url, download=False)
                video_title = info_dict.get('title', 'Unknown Title')
                self.status_callback(20)
                self.status_callback(None, f"'{video_title}' is being downloaded as {file_format}.")
                ydl.download([url])
        except Exception as e:
            self.status_callback(None, f"Error: {str(e)}")
    
    def getYDLOpts(self, file_format):
        ydl_opts = {
            'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
            'progress_hooks': [self.progress_hook],
            'noplaylist': True,
        }

        ydl_opts.update(self.formats.get(file_format, {'format': 'best'}))

        return ydl_opts