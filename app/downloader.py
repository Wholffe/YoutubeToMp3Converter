import yt_dlp
import os

class Downloader():
    def __init__(self):
        ffmpeg_path = os.path.join(os.path.dirname(__file__), '..', 'bin', 'ffmpeg')
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'ffmpeg_location': ffmpeg_path,
        }

    def download(self, url, path):
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            ydl.download([url])
