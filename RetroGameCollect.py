# RetroGameCollect (09-05-19)

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QLabel
from PyQt5.QtGui import QIcon, QPixmap
import sqlite3


def connect():
    conn = sqlite3.connect("rgc.db")
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS table1 (
                    format TEXT,
                    type TEXT,
                    title TEXT,
                    productid TEXT, 
                    grade INTEGER,
                    price INTEGER
                    )"""
    )
    conn.commit()
    conn.close()


def search(format="", type="", title="", productid="", grade="", price=""):
    conn = sqlite3.connect("rgc.db")
    c = conn.cursor()
    c.execute(
        "SELECT * FROM table1 WHERE title=? OR productid=? OR grade=? OR price=?",
        (title, productid, grade, price),
    )
    results = c.fetchall()
    conn.close()
    return results


connect()


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.setWindowTitle("Retro Game Collect")
        self.setFixedSize(900, 700)
        fileMenu = self.menuBar().addMenu("File")
        exitAction = QAction("- &Quit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.triggered.connect(qApp.quit)
        fileMenu.addAction(exitAction)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("./images/mainlogo.png"))
        self.label.setGeometry(50, 0, 800, 75)

        self.show()


app = QApplication(sys.argv)
home = Window()
sys.exit(app.exec_())
