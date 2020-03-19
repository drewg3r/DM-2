"""
 * Copyright © 2020 drewg3r
 * https://github.com/drewg3r/DM-2

main.py: main file to run the program.
"""

import sys
from PyQt5 import QtWidgets
import core, iface
from PyQt5.QtWidgets import *


app = QtWidgets.QApplication(sys.argv)
window = iface.MyApp()
window.show()
app.exec_()
