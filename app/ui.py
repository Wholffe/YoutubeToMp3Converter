from utils import get_default_dir
import constants as CONST
import PySimpleGUI as sg


EVENT_WINDOW_CLOSED = sg.WIN_CLOSED

def create_window():
    progress_bar = sg.ProgressBar(100, orientation='h', size=(20, 20), key=CONST.KEY_PROGRESS_BAR)
    destination_dir = get_default_dir()

    layout = [
        [sg.Text(CONST.BUTTON_VIDEO_URL), sg.InputText(key=CONST.KEY_VIDEO_URL)],
        [sg.Text(CONST.BUTTON_DEST_FOLDER), sg.InputText(key=CONST.KEY_DEST_FOLDER,default_text=destination_dir), sg.FolderBrowse(button_text=CONST.BUTTON_BROWSE)],
        [sg.Button(CONST.BUTTON_DOWNLOAD, key=CONST.KEY_DOWNLOAD), sg.Button(CONST.BUTTON_OPEN_DEST_FOLDER, key=CONST.KEY_OPEN_DEST_FOLDER), sg.Button(CONST.BUTTON_CANCEL, key=CONST.KEY_CANCEL)],
        [sg.Multiline(size=(40, 6), key=CONST.KEY_OUTPUT, disabled=True, autoscroll=True)],
        [progress_bar]
    ]

    window = sg.Window(CONST.BUTTON_TITLE, layout)
    return window
