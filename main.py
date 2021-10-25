import sys
import logging
from PyQt5 import QtWidgets
from ui import VCDManager


def ui_test():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        # datefmt='%Y-%m-%d %A %H:%M:%S'
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    app = QtWidgets.QApplication(sys.argv)
    w = VCDManager()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    ui_test()
