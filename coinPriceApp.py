import sys
import time

import requests
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyupbit
import json

form_class = uic.loadUiType("ui/coinPrice.ui")[0]

class CoinViewThread(QThread):
    coinDataSent = pyqtSignal(float, float, float, float, float, float, float, float)
    def __init__(self):
        super().__init__()
        self.ticker = "BTC"
        self.alive = True

    def run(self):

        while self.alive:
            url = "https://api.upbit.com/v1/ticker"
            param = {"markets":"KRW-BTC"}
            response = requests.get(url, params=param)
            upbitResult = response.json()

            trade_price = upbitResult[0]['trade_price']
            signed_change_rate = upbitResult[0]['signed_change_rate']
            acc_trade_volume_24h = upbitResult[0]['acc_trade_volume_24h']
            high_price = upbitResult[0]['high_price']
            highest_52_week_price = upbitResult[0]['highest_52_week_price']
            low_price = upbitResult[0]['low_price']
            lowest_52_week_price = upbitResult[0]['lowest_52_week_price']
            prev_closing_price = upbitResult[0]['prev_closing_price']


            # 슬롯에 코인정보 보내기
            self.coinDataSent.emit(float(trade_price),
                                   float(signed_change_rate),
                                   float(acc_trade_volume_24h),
                                   float(high_price),
                                   float(highest_52_week_price),
                                   float(low_price),
                                   float(lowest_52_week_price),
                                   float(prev_closing_price))

            time.sleep(10) #api 호출 1초 딜레이 (딜레이없으면 벤 당함)

        def close(self):
            self.alive = False

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Coin Price Overview")
        self.setWindowIcon(QIcon("icons/coin.png"))
        self.statusBar().showMessage("ver 0.5")

        self.cvt = CoinViewThread() #코인정보를 가져오는 쓰레드 클래스를 객체로 선언
        self.cvt.coinDataSent.connect(self.fillCoinData) #쓰레드시그널에서 온 데이터를 받아올 슬롯함수연결
        self.cvt.start() #쓰레드 클래스의 run()호출(함수시작)


    # 쓰레드클레스에서 보내준 데이터를 받아주는 슬롯 함수

    def fillCoinData(self, trade_price, signed_change_rate, acc_trade_volume_24h, high_price, highest_52_week_price, low_price, lowest_52_week_price, prev_closing_price):

        self.price_label.setText(f"{trade_price:,.0f}원")
        self.change_rate_label.setText(f"{signed_change_rate:+.2f}%")
        self.trade_volume_label.setText(f"{acc_trade_volume_24h:,}")
        self.high_price_label.setText(f"{high_price:,.0f}원")
        self.highest_52_label.setText(f"{highest_52_week_price:,.0f}원")
        self.low_price_label.setText(f"{low_price:,.0f}원")
        self.lowest_52_label.setText(f"{lowest_52_week_price:,.0f}원")
        self.closing_price_label.setText(f"{prev_closing_price:,.0f}원")
        self.__updateStyle()

    def __updateStyle(self):
        if '-' in self.change_rate_label.text():
            self.change_rate_label.setStyleSheet("background-color:blue; color:white")
            self.price_label.setStyleSheet("border:solid;border-color:rgb(123, 123, 255);border-width:2px;background-color:rgb(205, 205, 255); border-radius:10px;color:blue")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())