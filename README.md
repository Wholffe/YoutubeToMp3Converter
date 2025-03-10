# YoutubeToMp3Converter
A simple application with a graphical user interface that allows users to extract audio from YouTube videos and save it in different formats such as MP3, MP4, and WebM. This enables users to download music, podcasts, or other audio content from videos for offline listening in a portable format compatible with most media players.

<div style="display: flex;">
  <img src="assets\YTDownloader1.png" alt="YTDownloader1"/>
  <img src="assets\YTDownloader2.png" alt="YTDownloader2"/>
  <img src="assets\YTDownloader3.png" alt="YTDownloader3"/>
</div>

## How to use
1. Open the application.
2. Enter the URL of the YouTube video you want to convert.
3. Select the desired format (e.g., MP3, MP4, WebM) and quality.
4. Click the "Download" button.
5. The application will download and convert the video to the selected format.
6. The converted file will be saved to the specified download path.

## How to install
1. Ensure you have Python installed (Python 3.6 or higher is recommended).
2. Download the repository as a ZIP file and extract it.
3. Open a terminal and navigate to the extracted folder.
4. Install the required Python packages by running:
```
pip install -r requirements.txt
```

## Convert to .exe
- Open cmd in the current app path and run the following command:
```
pyinstaller -w -F --icon=".\path\to\your\icon.ico" main.py
```
- Replace `.\path\to\your\icon.ico` with the actual path to your icon file.

## Contribution
Contributions to this repository are welcome! If you have additional ideas or improvements, feel free to submit pull requests.

## License
This repository is licensed under the [MIT License](./LICENSE).