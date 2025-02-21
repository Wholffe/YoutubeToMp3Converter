from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QColor
from PyQt6 import uic

from downloader import Downloader

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("app/ui/mainWindow.ui", self)
        with open("app/styles.css","r") as f:
            self.setStyleSheet(f.read())
        self.comboBoxFormat.addItems(["MP4", "MP3", "WebM"])
        self.comboBoxQuality.addItems(["Audio Only","1080p", "720p","480p"])
        self.lineEditVideoUrl.textChanged.connect(self.onTextChanged)
        self.lineEditVideoUrl.setFocus()
        self.buttonDownload.clicked.connect(self.onDownloadClicked)
        self.progressBar.hide()
        self.downloader = Downloader()
        self.appendText(f"Download Path: {self.downloader.download_path}")

    def onTextChanged(self, text):
        self.buttonDownload.setEnabled(len(text) > 0)
    
    def onDownloadClicked(self):
        print(self.downloader.download_path)
        self.appendText(f"Downloading {self.lineEditVideoUrl.text()}")
        self.progressBar.show()
        self.downloader.download(self.lineEditVideoUrl.text(), self.downloader.download_path)
        self.appendText(f"File Content {self.downloader.download_path}", "green")
    
    def appendText(self, text, color=''):
        match color:
            case 'red':
                self.textEditLog.setTextColor(QColor(255,0,0))
            case 'green':
                self.textEditLog.setTextColor(QColor(0,255,0))
            case _:
                self.textEditLog.setTextColor(self.textEditLog.palette().text().color())
        self.textEditLog.append(text)