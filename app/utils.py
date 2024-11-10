import os
import re
import threading
from pytubefix import YouTube
import constants as CONST

def get_default_dir():
    #set_working_directory()  # Set the working directory first
    parent_directory = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(parent_directory, 'YT_Downloads')

def open_folder(window, folder_path):
    if os.path.exists(folder_path):
        os.system(f'Explorer "{folder_path}"')
    else:
        window[CONST.KEY_OUTPUT].print(f'The folder does not exist: {folder_path}')

def is_valid_youtube_url(url):
    youtube_url_patterns = [
        r'^https?://www\.youtube\.com/watch\?v=.*',
        r'^https?://youtu\.be/.*'
    ]

    for pattern in youtube_url_patterns:
        if re.match(pattern, url):
            return True
    return False

def check_if_dir_exists(window, path):
    if not os.path.exists(path):
        try:
            os.makedirs(path)
            window[CONST.KEY_OUTPUT].print(f'{CONST.MESSAGE_PATH_CREATED} {path}')
        except OSError as e:
            window[CONST.KEY_OUTPUT].print(f'{CONST.ERROR_CREATING_PATH} {path}: {e}')
    return path

def get_only_audio_stream(youtube_link: str):
    return youtube_link.streams.get_audio_only()

def download_mp3_from_ytlink(only_audio_stream, destination_path):
    return only_audio_stream.download(output_path=destination_path)

def convert_to_mp3_and_remove_double_data(window, file_path: str) -> None:
    base, _ = os.path.splitext(file_path)
    new_file = base + '.mp3'
    if os.path.exists(new_file):
        window[CONST.KEY_OUTPUT].print(CONST.MESSAGE_FILE_EXISTS)
    else:
        os.rename(file_path,new_file)

def start_download(window, video_url, destination_folder):
    try:
        youtube_link = YouTube(video_url)
        destination_folder = check_if_dir_exists(window, destination_folder)
        window[CONST.KEY_OUTPUT].print(f'{CONST.MESSAGE_DOWNLOADING} {youtube_link.title} as mp3')
        window[CONST.KEY_PROGRESS_BAR].update_bar(20) 
        only_audio_stream = get_only_audio_stream(youtube_link)
        window[CONST.KEY_PROGRESS_BAR].update_bar(30) 
        out_file = download_mp3_from_ytlink(only_audio_stream, destination_folder)
        window[CONST.KEY_PROGRESS_BAR].update_bar(60) 
        convert_to_mp3_and_remove_double_data(window, out_file)
        window[CONST.KEY_PROGRESS_BAR].update_bar(70) 
        window[CONST.KEY_OUTPUT].print(CONST.MESSAGE_DOWNLOADING_COMPLETED)
        window[CONST.KEY_OUTPUT].print(f'{CONST.MESSAGE_DEST_FOLDER} {destination_folder}')
        window[CONST.KEY_PROGRESS_BAR].update_bar(100) 
    except Exception as e:
        window[CONST.KEY_OUTPUT].print(f'{CONST.ERROR_DOWNLOAD_FAILED} {str(e)}')

def download_thread(window, video_url, destination_folder):
    threading.Thread(target=start_download, args=(window, video_url, destination_folder)).start()

def get_default_dir():
    return os.path.join(os.getcwd(), 'YT_Downloads')