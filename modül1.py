import sys
import main as m
import cv2
from PyQt5.QtWidgets import QApplication, QDialog


class Life2Coding(QDialog):
    def __init__(self):
        super(Life2Coding, self).__init__()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    Root = m.MainWindow()
    Root.show()
    
    sys.exit(App.exec())


