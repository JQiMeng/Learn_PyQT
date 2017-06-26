import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(600,520)
    w.move(100,150)
    w.setWindowTitle('sample')
    w.show()

    sys.exit(app.exec_())