import PySimpleGUI as sgui
from utils import get_default_dir, open_folder, is_valid_youtube_url, download_thread
from ui import create_window
import constants as CONST

destination_dir = get_default_dir()
window = create_window()

running = True
while running:
    event, values = window.read()

    if event in (sgui.WINDOW_CLOSED, 'Cancel'):
        running = False

    video_url = values['video_url']
    destination_folder = values['destination_folder']

    if event == 'Open Destination Folder':
        window["output"].print(CONST.MESSAGE_OPEN_DEST_FOLDER)
        open_folder(window, destination_folder)

    if event == 'Download':
        console_output = ''

        if not video_url:
            console_output += CONST.ERROR_VIDEO_URL_EMPTY
        elif not destination_folder:
            console_output += CONST.ERROR_DEST_FOLDER_EMPTY
        elif not is_valid_youtube_url(video_url):
            console_output += CONST.ERROR_INVALID_VIDEO_URL
        else:
            window['progress_bar'].update_bar(0)
            download_thread(window, video_url, destination_folder)

        window['output'].update(console_output)

window.close()
