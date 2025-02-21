from PyQt6.QtWidgets import QDialog,QFileDialog
from PyQt6 import uic

class SettingsDialog(QDialog):
    def __init__(self,downloader):
        super().__init__()
        uic.loadUi("app/ui/settingsDialog.ui", self)
        with open("app/styles.css", "r") as f:
            self.setStyleSheet(f.read())
        self.downloader = downloader
        self.lineEditCurrentPath.setText(self.downloader.download_path)
        self.buttonDirectory.clicked.connect(self.selectPath)
        self.buttonBox.accepted.connect(self.changePath)
        self.buttonBox.rejected.connect(self.resetPath)

    def show(self):
        self.lineEditCurrentPath.setText(self.downloader.download_path)
        self.exec()

    def selectPath(self):
        current_path = self.downloader.download_path
        folder_path = QFileDialog.getExistingDirectory(self, "Get Existing Directory", current_path)
        if folder_path:
            self.lineEditCurrentPath.setText(folder_path)
    
    def changePath(self):
        self.downloader.download_path = self.lineEditCurrentPath.text()
        self.lineEditCurrentPath.setText(self.downloader.download_path)
    
    def resetPath(self):
        self.lineEditCurrentPath.setText(self.downloader.download_path)
        