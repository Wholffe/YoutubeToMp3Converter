import PySimpleGUI as sg
from utils import get_default_dir
import constants as CONST

def create_window():
    progress_bar = sg.ProgressBar(100, orientation='h', size=(20, 20), key=CONST.KEY_PROGRESS_BAR)
    destination_dir = get_default_dir()

    layout = [
        [sg.Text('Video URL'), sg.InputText(key=CONST.KEY_VIDEO_URL)],
        [sg.Text('Destination Folder'), sg.InputText(key=CONST.KEY_DEST_FOLDER, default_text=destination_dir), sg.FolderBrowse(button_text="Browse")],
        [sg.Button('Download', key=CONST.KEY_DOWNLOAD), 
         sg.Button('Open Destination Folder', key=CONST.KEY_OPEN_DEST_FOLDER), 
         sg.Button('Cancel', key=CONST.KEY_CANCEL)
         ],
        [sg.Multiline(size=(40, 6), key=CONST.KEY_OUTPUT, disabled=True, autoscroll=True)],
        [progress_bar]
    ]

    window = sg.Window('YouTube Downloader', layout)
    return window
