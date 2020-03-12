import sys
from PyQt5 import QtWidgets
import core, interface.w1
from PyQt5.QtWidgets import *


def showError(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Помилка!")
    msg.setInformativeText(text)
    msg.setWindowTitle("Помилка")
    msg.exec_()


class MyApp(QtWidgets.QMainWindow, interface.w1.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Adding items to men and women listWidgets
        for i in core.men_names:
            self.listWidget_men_names.addItem(i)
        for i in core.women_names:
            self.listWidget_women_names.addItem(i)