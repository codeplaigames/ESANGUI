import sys
from PyQt5.QtWidgets import QApplication, QWidget

class GUI(QWidget):
    def __init__(self):
        super().__init__()
        #initializae super class
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('PyQt5 GUI')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())