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

        # Linking buttons to functions
        self.pushButton_var_clc.clicked.connect(self.var_clc_btn)

        self.pushButton_cpy.clicked.connect(self.cpy_btn)

        self.pushButton_read_a.clicked.connect(self.read_a_btn)
        self.pushButton_save_a.clicked.connect(self.save_a_btn)
        self.pushButton_clear_a.clicked.connect(self.clear_a_btn)

        self.pushButton_read_b.clicked.connect(self.read_b_btn)
        self.pushButton_save_b.clicked.connect(self.save_b_btn)
        self.pushButton_clear_b.clicked.connect(self.clear_b_btn)

        self.pushButton_mtr_s.clicked.connect(self.mtr_s_btn)
        self.pushButton_mtr_r.clicked.connect(self.mtr_r_btn)
        self.pushButton_mtr_rus.clicked.connect(self.mtr_rus_btn)
        self.pushButton_mtr_rds.clicked.connect(self.mtr_rds_btn)
        self.pushButton_mtr_rms.clicked.connect(self.mtr_rms_btn)
        self.pushButton_mtr_umr.clicked.connect(self.mtr_umr_btn)
        self.pushButton_mtr_st.clicked.connect(self.mtr_st_btn)

        self.pushButton_abt.clicked.connect(self.abt_btn)

    def var_clc_btn(self):
        try:
            G = int(self.lineEdit_grp_num.text())
            N = int(self.lineEdit_ord_num.text()) + 2
            self.label_9.setText(str((N + G % 60) % 30 + 1))
        except:
            self.label_9.setText("??")

    def cpy_btn(self):
        """Function for copy button"""
        smen = [item.text() for item in self.listWidget_men_names.selectedItems()]
        swomen = [item.text() for item in self.listWidget_women_names.selectedItems()]
        try:
            smen.remove("- None -")
            swomen.remove("- None -")
        except:
            pass
        if self.radioButton_a.isChecked():
            core.A = core.A.union(set(smen + swomen))
            self.listWidget_set_a.clear()
            self.listWidget_set_a.addItems(list(core.A))

        if self.radioButton_b.isChecked():
            core.B = core.B.union(set(smen + swomen))
            self.listWidget_set_b.clear()
            self.listWidget_set_b.addItems(list(core.B))

    def read_a_btn(self):
        pass

    def save_a_btn(self):
        pass

    def clear_a_btn(self):
        pass

    def read_b_btn(self):
        pass

    def save_b_btn(self):
        pass

    def clear_b_btn(self):
        pass

    def mtr_s_btn(self):
        pass

    def mtr_r_btn(self):
        pass

    def mtr_rus_btn(self):
        pass

    def mtr_rds_btn(self):
        pass

    def mtr_rms_btn(self):
        pass

    def mtr_umr_btn(self):
        pass

    def mtr_st_btn(self):
        pass

    def abt_btn(self):
        pass
