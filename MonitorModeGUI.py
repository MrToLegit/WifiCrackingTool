import sys
import math
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
import os
import platform

if platform.system() != "Linux":
    print("You can run this script only on Linux based devices.")
    quit()

if __name__ == '__main__':
    
    def center(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(200, 100)
    center(w)
    
    btn = QPushButton('Quit', w)
    btn.clicked.connect(QApplication.instance().quit)
    btn.resize(btn.sizeHint())
    btn.move(w.width() / 2 - btn.width()/2, w.height() -35) 

    def monitormode():
        os.system("airmon-ng check kill")
        os.system("iwconfig wlan0 mode monitor")

    def automode():
        os.system("iwconfig wlan0 mode auto")
        os.system("service network-manager start")

    btnsave = QPushButton('Set to Monitor Mode', w)
    btnsave.clicked.connect(lambda: monitormode())
    btnsave.resize(btnsave.sizeHint())
    btnsave.move(w.width() / 2 - btnsave.width()/2, 2) 

    btnload = QPushButton('Set to Auto Mode', w)
    btnload.clicked.connect(lambda: automode())
    btnload.resize(btnload.sizeHint()) 
    btnload.move(w.width() / 2 - btnload.width()/2, w.height() / 2 - btnload.height() / 2) 

    w.setWindowTitle('Test')
    w.setFixedSize(w.size())
    w.show()

    sys.exit(app.exec_())
