import sys
import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __int__(self):
        super().__init__()
        


def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.show()
    sys.exit(app.exec_())
       

if __name__ == "__main__":
    main()
