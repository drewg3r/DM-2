"""
 * Copyright © 2020 drewg3r
 * https://github.com/drewg3r/DM-2

Interface for 'about' window.
"""

from PyQt5 import QtWidgets
import interface
from interface.about import Ui_Form


class MyFormAbout(QtWidgets.QMainWindow, interface.about.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close_btn)

    def close_btn(self):
        self.close()
