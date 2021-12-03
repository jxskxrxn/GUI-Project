from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import qdarkstyle

from video import VideoPlayer


class Demo(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setWindowIcon(QIcon('logo.png'))
        self.dirpath = QDir.currentPath()
        self.filter_name = 'Images (*.jpeg *.png *.jpg *.gif)'
        self.filter_video_name = 'Videos (*.avi *.wmv)'
        self.grid = QGridLayout()
        self.label = QLabel()

        # Ensure our window stays in front and give it a title
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowTitle("File Browser")
        self.setFixedSize(400, 300)
        self.statusBar().showMessage('Ready')

        self.imagebutton = QPushButton('Open Images', self)
        self.imagebutton.clicked.connect(self.get_image)
        self.imagebutton.resize(200, 32)
        self.imagebutton.move(100, 100)

        self.videobutton = QPushButton('Open Videos', self)
        self.videobutton.clicked.connect(self.get_video)
        self.videobutton.resize(200, 32)
        self.videobutton.move(100, 140)

        self.themebutton = QCheckBox('Enable Dark Mode', self)
        self.themebutton.clicked.connect(self.change_theme)
        self.themebutton.resize(200, 32)
        self.themebutton.move(100, 180)

        self.helpbutton = QPushButton(QIcon('help.png'), '', self)
        self.helpbutton.clicked.connect(self.show_dialog)
        self.helpbutton.resize(50, 32)
        self.helpbutton.move(320, 250)

        self.tb = self.addToolBar("File")
        self.new = QAction(QIcon("new.png"), "new", self)
        self.tb.addAction(self.new)
        self.tb.setStatusTip('New')

        self.open = QAction(QIcon("open.png"), "open", self)
        self.tb.addAction(self.open)
        self.tb.setStatusTip('Open')

        self.save = QAction(QIcon("save.png"), "save", self)
        self.tb.addAction(self.save)
        self.tb.setStatusTip('Save')

        # Create exit action
        self.exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.setStatusTip('Exit application')
        self.exitAction.triggered.connect(self.close)

        # Create menu bar and add action
        self.menuBar = self.menuBar()
        fileMenu = self.menuBar.addMenu('&Menu')
        fileMenu.addAction(self.exitAction)

    def show_dialog(self):
        dlg = QDialog()
        dlg.setWindowTitle("About")
        dlg.resize(200, 100)
        message = QLabel("This is a simple PyQT5 app which \n can open images and video files.", dlg)
        message.move(20, 20)
        dlg.setWindowFlags(Qt.WindowStaysOnTopHint)
        dlg.exec_()

    def get_image(self):
        path = QFileDialog.getOpenFileName(self, directory=self.dirpath, filter=self.filter_name)[0]
        print(path)
        dialog = QDialog()
        dialog.setWindowFlags(Qt.WindowStaysOnTopHint)
        label = QLabel()
        pixmap = QPixmap(path)
        pixmap = pixmap.scaled(600, 400, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap)
        layout = QVBoxLayout()
        dialog.setLayout(layout)
        layout.addWidget(label)
        dialog.setFixedSize(600, 400)
        dialog.exec_()

    def get_video(self):
        path = QFileDialog.getOpenFileName(self, directory=self.dirpath, filter=self.filter_video_name)[0]
        print(path)
        self.video_player(path)

    def video_player(self, path):
        self.player = VideoPlayer(path)
        self.player.show()
        self.hide()
        self.player.resize(600, 400)

    def change_theme(self):
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        if not self.themebutton.isChecked():
            app.setStyleSheet("")


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    demo = Demo()  # <<-- Create an instance
    demo.show()
    sys.exit(app.exec_())
