from utils import open_folder, is_valid_youtube_url, download_thread
import constants as CONST
import ui


def main():
    window = ui.create_window()
    running = True

    while running:
        event, values = window.read()

        if event in (ui.EVENT_WINDOW_CLOSED, CONST.KEY_CANCEL):
            running = False

        video_url = values[CONST.KEY_VIDEO_URL]
        destination_folder = values[CONST.KEY_DEST_FOLDER]

        if event == CONST.KEY_OPEN_DEST_FOLDER:
            open_folder(window, destination_folder)

        if event == CONST.KEY_DOWNLOAD:
            console_output = ''

            if not video_url:
                console_output += CONST.ERROR_VIDEO_URL_EMPTY
            elif not destination_folder:
                console_output += CONST.ERROR_DEST_FOLDER_EMPTY
            elif not is_valid_youtube_url(video_url):
                console_output += CONST.ERROR_INVALID_VIDEO_URL
            else:
                window[CONST.KEY_PROGRESS_BAR].update_bar(0)
                download_thread(window, video_url, destination_folder)

            window[CONST.KEY_OUTPUT].update(console_output)

    window.close()

if __name__ == "__main__":
    main()
