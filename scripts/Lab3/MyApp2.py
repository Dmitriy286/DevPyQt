import time
from PySide2 import QtWidgets, QtCore
import psutil
import requests

from scripts.Lab3.ui.P3_HardwareIndependentIO_QThread_design import Ui_Form

# ЗАДАНИЯ:
# 1. Реализовать таймер до 0 с возможностью остановки
# 2. Бесконечная проверка доступности сайта с возможностью остановки и установки времени задержки (при запуске)
# 3. Получение системных параметров (запуск при старте программы), предусмотреть "горячий" режим установки времени задержки

# Все 3 блока должны быть реализованы в одном окне и работать одновременно друг с другом

class MyApp2(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.initThread()
        self.initSignals()




    def initSignals(self):
        # init signals
        self.ui.pushButtonStart.clicked.connect(self.onPushButtonStartClicked)
        self.ui.pushButtonStop.clicked.connect(self.onPushButtonStopClicked)

        self.ui.pushButtonUrlStart.clicked.connect(self.onPushButtonUrlStartClicked)
        self.ui.pushButtonUrlStop.clicked.connect(self.onPushButtonUrlStopClicked)




    def initThread(self):
        self.threadOne = TimerThread()
        self.threadTwo = SiteChecking()
        self.threadThree = CPUandRAMChecking()
        self.threadThree.start()


    def onPushButtonStartClicked(self):
        self.threadOne.start()

    def onPushButtonStopClicked(self):
        ...


    def onPushButtonUrlStartClicked(self):
        self.threadTwo.start()

    def onPushButtonUrlStopClicked(self):
        ...




class TimerThread(QtCore.QThread):

    def __init__(self, parent=None):
        super(TimerThread, self).__init__(parent)


    def run(self):
        for i in range(10, 0, -1):
            print(i)
            time.sleep(1)


class SiteChecking(QtCore.QThread):
    def __init__(self, parent=None):
        super(SiteChecking, self).__init__(parent)

    def run(self):
        r = requests.get('https://www.python.org')
        print(r.status_code)


class CPUandRAMChecking(QtCore.QThread):
    def __init__(self, parent=None):
        super(CPUandRAMChecking, self).__init__(parent)

    def run(self):
        print(psutil.cpu_percent(interval=None, percpu=False))
        print(psutil.swap_memory().percent)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = MyApp2()
    myapp.show()

    app.exec_()
