import PySimpleGUI as sg
from utils import get_default_dir
import constants as CONST

def create_window():
    progress_bar = sg.ProgressBar(100, orientation='h', size=(20, 20), key='progress_bar')
    destination_dir = get_default_dir()

    layout = [
        [sg.Text('Video URL'), sg.InputText(key='video_url')],
        [sg.Text('Destination Folder'), sg.InputText(key='destination_folder', default_text=destination_dir), sg.FolderBrowse(button_text="Browse")],
        [sg.Button('Download'), 
         sg.Button('Open Destination Folder'), 
         sg.Button('Cancel')
         ],
        [sg.Multiline(size=(40, 6), key=CONST.KEY_OUTPUT, disabled=True, autoscroll=True)],
        [progress_bar]
    ]

    window = sg.Window('YouTube Downloader', layout)
    return window
