import sys
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import json

form_class = uic.loadUiType("ui/coinPrice.ui")[0]

class CoinViewThread(QThread):
    def __init__(self):
        super().__init__()
        self.ticker = "BTC"
        self.alive = True




class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Coin Price Overview")
        self.setWindowIcon(QIcon("icons/coin.png"))
        self.statusBar().showMessage("ver 0.5")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())