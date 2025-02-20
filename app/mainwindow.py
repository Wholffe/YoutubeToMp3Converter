from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

from downloader import Downloader

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("app/ui/mainWindow.ui", self)
        self.lineEditVideoUrl.textChanged.connect(self.onTextChanged)
        self.buttonDownload.clicked.connect(self.onDownloadClicked)

        self.downloader = Downloader()
        self.downloadPath = "Downloads" #TODO Dynamic path

    def onTextChanged(self, text):
        self.buttonDownload.setEnabled(len(text) > 0)
        print(text)
    
    def onDownloadClicked(self):
        print("start Downloading")
        self.downloader.download(self.lineEditVideoUrl.text(), self.downloadPath)