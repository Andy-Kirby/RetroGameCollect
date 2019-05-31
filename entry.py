from PyQt5.QtWidgets import (
    QWidget,
    QApplication,
    QMainWindow,
    QAction,
    qApp,
    QLabel,
    QPushButton,
)
from PyQt5.QtGui import QIcon, QPixmap
import sqlite3


class Entry(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.setWindowTitle("Create New Entry")
        self.setFixedSize(700, 500)
        fileMenu = self.menuBar().addMenu("File")
        exitAction = QAction("- &Quit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.triggered.connect(qApp.quit)
        fileMenu.addAction(exitAction)

        self.show()
