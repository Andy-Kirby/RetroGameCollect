# RetroGameCollect (09-05-19)

import sys
from PyQt5.QtWidgets import (
    QWidget,
    QApplication,
    QMainWindow,
    QAction,
    qApp,
    QLabel,
    QPushButton,
    QComboBox,
    QListView,
    QGroupBox,
    QRadioButton,
    QTableWidget,
    QTableView,
    QLineEdit,
)
from PyQt5.QtCore import QSize, QRect
from PyQt5.QtGui import QIcon, QPixmap, QFont
import sqlite3
from entry import Entry

# SQLITE (BACKEND)


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

# MAIN


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def entryWindow(self, entry):
        self.newWindow = Entry()

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

    def init_ui(self):

        self.setWindowTitle("Retro Game Collect")
        self.setFixedSize(900, 700)
        fileMenu = self.menuBar().addMenu("File")
        exitAction = QAction("- &Quit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.triggered.connect(qApp.quit)
        fileMenu.addAction(exitAction)
        # Header
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("./img/header.png"))
        self.label.setGeometry(0, 0, 900, 85)
        # Main Logo
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("./img/mainlogo.png"))
        self.label.setGeometry(38, 20, 387, 42)
        # Group Box (Tools)
        self.group_box_settings = QGroupBox(self)
        self.group_box_settings.setTitle("Tools")
        self.group_box_settings.setGeometry(40, 75, 195, 65)
        # Tool Buttons
        self.add_button = QPushButton("", self)
        self.add_button.setIcon(QIcon("./img/add.png"))
        self.add_button.setIconSize(QSize(12, 12))
        self.add_button.resize(60, 30)
        self.add_button.move(50, 100)
        self.add_button.setToolTip("Create")
        self.add_button.clicked.connect(self.entryWindow)

        self.add_button = QPushButton("", self)
        self.add_button.setIcon(QIcon("./img/edit.png"))
        self.add_button.setIconSize(QSize(12, 12))
        self.add_button.resize(60, 30)
        self.add_button.move(110, 100)
        self.add_button.setToolTip("Edit")
        self.add_button.clicked.connect(self.entryWindow)

        self.add_button = QPushButton("", self)
        self.add_button.setIcon(QIcon("./img/delete.png"))
        self.add_button.setIconSize(QSize(12, 12))
        self.add_button.resize(60, 30)
        self.add_button.move(165, 100)
        self.add_button.setToolTip("Delete")
        self.add_button.clicked.connect(self.entryWindow)

        # Group Box (Format)
        self.group_box_settings = QGroupBox(self)
        self.group_box_settings.setTitle("Format")
        self.group_box_settings.setGeometry(270, 75, 340, 65)
        # Combo Box
        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(QRect(280, 100, 320, 31))
        self.comboBox.setObjectName(("comboBox"))
        self.comboBox.addItem("Please Select...")
        self.comboBox.addItem("Sega Master System")
        self.comboBox.addItem("Sega Megadrive")
        self.comboBox.addItem("Sega Saturn")
        self.comboBox.addItem("Sega Dreamcast")
        self.comboBox.addItem("Sega Game Gear")
        self.comboBox.addItem("Nintendo NES")
        self.comboBox.addItem("Super Nintendo")
        self.comboBox.addItem("Nintendo64")
        self.comboBox.addItem("Nintendo Game Cube")
        self.comboBox.addItem("Nintendo Game Boy")
        self.comboBox.addItem("PlayStation 1")
        self.comboBox.addItem("PSOne")
        self.comboBox.addItem("Microsoft XBOX")
        self.comboBox.activated.connect(self.handleActivated)

        # Group Box (Radio Buttons)
        self.group_box_settings = QGroupBox(self)
        self.group_box_settings.setTitle("")
        self.group_box_settings.setGeometry(645, 93, 215, 47)
        # Radio Buttons
        self.software = QRadioButton("Software", self)
        self.software.setChecked(True)
        self.software.move(665, 100)
        self.hardware = QRadioButton("Hardware", self)
        self.hardware.move(760, 100)

        # Group Box (SQLite3 Table)
        self.group_box_settings = QGroupBox(self)
        self.group_box_settings.setTitle("Results")
        self.group_box_settings.setGeometry(270, 160, 590, 440)
        # SQLite3 Table
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(QRect(285, 190, 560, 359))
        self.tableWidget.setRowCount(16)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setColumnWidth(0, 298)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 80)
        self.tableWidget.setColumnWidth(3, 80)
        self.tableWidget.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget.verticalHeader().hide()
        header = ["Title", "Product ID", "Grade", "Paid"]
        self.tableWidget.setHorizontalHeaderLabels(header)
        self.tableWidget.setSelectionBehavior(QTableView.SelectRows)
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        # Total Games
        self.labelT = QLabel(self)
        self.labelT.setPixmap(QPixmap("./img/quantity.png"))
        self.labelT.setGeometry(285, 555, 124, 32)
        self.tableTotal = QLineEdit(self)
        self.tableTotal.setGeometry(420, 562, 80, 20)
        self.tableTotal.setReadOnly(True)
        # Total Spent
        self.labelT = QLabel(self)
        self.labelT.setPixmap(QPixmap("./img/paid.png"))
        self.labelT.setGeometry(590, 555, 166, 32)
        self.tableTotal = QLineEdit(self)
        self.tableTotal.setGeometry(765, 562, 80, 20)
        self.tableTotal.setReadOnly(True)
        # Footer
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("./img/footer.png"))
        self.label.setGeometry(0, 620, 900, 85)
        # Andy Kirby 2019
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("./img/credit.png"))
        self.label.setGeometry(790, 665, 90, 23)
        self.show()

    def handleActivated(self):
        self.comboText = text


app = QApplication(sys.argv)
app.setStyle("macintosh")
home = Window()
sys.exit(app.exec_())
