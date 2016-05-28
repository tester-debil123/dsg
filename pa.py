# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, \
QGridLayout, QMainWindow, QAction, QToolTip, QApplication,\
QInputDialog, QLineEdit, QLabel, QSlider)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

class Example(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.method()
    def method(self):
        l1 = QLabel('<font color = green>Успешно</font>', self)
        lab = QLineEdit('', self)
        lab.setEchoMode(2)
        btn =  QPushButton('Cope', self)
        btn.setIcon(QIcon('цуи.png'))
        btn.clicked.connect(self.showDialog)
        sld = QSlider(Qt.Horizontal, self)
        sld.valueChanged[int].connect(self.showDialog)
        lab.move(100, 100)
        btn.move(300, 300)
        l1.move(300, 100)
        self.setFixedSize(720, 480)
        self.setWindowTitle('name')
        self.setToolTip('Главное окошко')

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        if ok:
            l1.setText(str(text))

#    def showDialog2(self):
#        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
#        print(fname)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
