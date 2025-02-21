from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QColor
from PyQt6 import uic

from downloader import Downloader

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("app/ui/mainWindow.ui", self)
        with open("app/styles.css", "r") as f:
            self.setStyleSheet(f.read())
        self.comboBoxFormat.addItems(["WebM"])
        self.comboBoxQuality.addItems(["Audio Only"])
        self.lineEditVideoUrl.textChanged.connect(self.onTextChanged)
        self.lineEditVideoUrl.setFocus()
        self.buttonDownload.clicked.connect(self.onDownloadClicked)
        self.progressBar.hide()
        self.downloader = Downloader()
        self.appendText(f"Download path: {self.downloader.download_path}")
        self.baseUrl = ["https://www.youtube.com/watch?v=", "https://youtu.be/"]

    def onTextChanged(self, text):
        ok = any(text.startswith(base) for base in self.baseUrl) and (text != self.downloader.current_download_url)
        self.buttonDownload.setEnabled(ok)

    def onDownloadClicked(self):
        self.buttonDownload.setEnabled(False)
        self.appendText(f"Start download ...'{self.lineEditVideoUrl.text()}'")
        self.progressBar.show()
        self.downloader.download(self.lineEditVideoUrl.text(), self.downloader.download_path, self.update_progress)

    def update_progress(self, percent, message=None):
        if message and "Error" in message:
            self.progressBar.setValue(0)
            self.progressBar.hide()
            self.appendText(f"Error: {message}", "red")
        elif percent is not None:
            self.progressBar.setValue(percent)
        elif message:
            self.appendText(message, "green")

    def appendText(self, text, color=''):
        match color:
            case 'red':
                self.textEditLog.setTextColor(QColor(255, 0, 0))
            case 'green':
                self.textEditLog.setTextColor(QColor(0, 255, 0))
            case _:
                self.textEditLog.setTextColor(self.textEditLog.palette().text().color())
        self.textEditLog.append(text)