import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
gui = QWidget()
gui.setWindowTitle('PyQt5 GUI')
gui.show()
sys.exit(app.exec_())