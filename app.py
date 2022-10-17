from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt6.QtCore import QSize, Qt
import sys



class MainPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle('Random Wiki')

        button = QPushButton('Next')
        button.setCheckable(True)
        button.clicked.connect(self.eventButton)
        self.setMinimumSize(QSize(700,700))

        self.setCentralWidget(button)


    def eventButton(self):
        print('Button event')

app = QApplication(sys.argv)

win = MainPage()
win.show()

app.exec()