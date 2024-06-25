from pytube import YouTube
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QProgressBar, QLineEdit, QFileDialog
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        
        uic.loadUi('youtube.ui', self)
        
        self.progress_bar = self.findChild(QProgressBar, "progressBar")
        self.url_link_field = self.findChild(QLineEdit, "url_link_field")
        self.url_title = self.findChild(QLabel, "url_title")
        self.download_btn = self.findChild(QPushButton, "download_btn")
        self.get_btn = self.findChild(QPushButton, "get_btn")
        
        self.get_btn.clicked.connect(self.get_video)
        self.download_btn.clicked.connect(self.download)
        
        self.show()
        
    def get_video(self):
        link = self.url_link_field.text()
        if link:
            video = YouTube(link).streams.filter(adaptive=True, file_extension='mp4').order_by('resolution').desc().first()
            self.url_title.setText(f"Title: {video.title}")
                
    def download(self):
        link = self.url_link_field.text()
        if link:
            video = YouTube(link).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            location = self.get_location()
            if location:
                video.download(location)
            else: 
                location = self.get_location()
        
    def get_location(self):
        directory = QFileDialog.getExistingDirectory(None, "Choose location")
        return directory
        
# video = YouTube("https://youtu.be/lEDH-vq5l6M?si=UYspS4ablbApuYdm").streams.filter(adaptive=True, file_extension='mp4').order_by('resolution').desc().first()
# print(video)
# video.download('')



app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()