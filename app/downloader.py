import yt_dlp
import os
from pathlib import Path

class Downloader():
    def __init__(self):
        self.download_path = str(Path.home() / "Downloads/ytdownloader")
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
        }

    def download(self, url, path):
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                ydl.download([url])
        except Exception as e:
            print(e)