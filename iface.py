import sys
from PyQt5 import QtWidgets
import core, interface.w1, interface.about
import ab_iface
import fr_generator
from PyQt5.QtWidgets import *
import networkx as nx
import matplotlib.pyplot as plt


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

        self.read_a_btn()
        self.read_b_btn()

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

        core.S, core.R = fr_generator.generate(
            core.A, core.B, core.s_possibility, core.r_possibility
        )

    def read_a_btn(self):
        """Reads file's content to set A and to A's listWidget"""
        try:
            with open(core.a_filename, "r") as f:
                core.A = set(list(f.read().split(", ")))
                core.A = core.A - set("")
                self.listWidget_set_a.clear()
                self.listWidget_set_a.addItems(list(core.A))
        except:
            pass

        core.S, core.R = fr_generator.generate(
            core.A, core.B, core.s_possibility, core.r_possibility
        )

    def save_a_btn(self):
        """Saves set A content to file"""
        with open(core.a_filename, "w+") as f:
            s = ""
            for e in core.A:
                s = s + str(e) + ", "
            s = s[:-2]
            f.write(s)

    def clear_a_btn(self):
        """Clearing set A and A's listWidget"""
        core.A = set()
        self.listWidget_set_a.clear()

        core.S, core.R = fr_generator.generate(
            core.A, core.B, core.s_possibility, core.r_possibility
        )

    def read_b_btn(self):
        """Reads file's content to set B and to B's listWidget"""
        try:
            with open(core.b_filename, "r") as f:
                core.B = set(list(f.read().split(", ")))
                core.B = core.B - set("")
                self.listWidget_set_b.clear()
                self.listWidget_set_b.addItems(list(core.B))
        except:
            pass
        core.S, core.R = fr_generator.generate(
            core.A, core.B, core.s_possibility, core.r_possibility
        )

    def save_b_btn(self):
        """Saves set B content to file"""
        with open(core.b_filename, "w+") as f:
            s = ""
            for e in core.B:
                s = s + str(e) + ", "
            s = s[:-2]
            f.write(s)

    def clear_b_btn(self):
        """Clearing set B and B's listWidget"""
        core.B = set()
        self.listWidget_set_b.clear()

        core.S, core.R = fr_generator.generate(
            core.A, core.B, core.s_possibility, core.r_possibility
        )

    def mtr_s_btn(self):
        """
        Drawing plot for S!
        Not optimized plot generator
        """
        P = core.S

        P = list(P)
        P.sort()

        plt.figure("Set S = Fathers-Children", figsize=(8, 4))

        g = nx.DiGraph()
        g.add_nodes_from(core.A)
        g.add_nodes_from(core.B)
        g.add_edges_from(P)

        color_map = []
        pos = {}
        i = 0
        j = 0
        for node in g:
            if node in core.A:
                i += 1
                pos[node] = (i, 2)
                color_map.append("blue")
            else:
                j += 1
                pos[node] = (j, 1)
                color_map.append("green")

        nx.draw(
            g,
            with_labels=True,
            node_size=2500,
            font_size=12,
            node_color=color_map,
            pos=pos,
        )
        plt.show()

    def mtr_r_btn(self):
        """
        Drawing plot for R!
        Not optimized plot generator
        """
        P = core.R

        P = list(P)
        P.sort()

        plt.figure("Set R = Fathers-in-law", figsize=(8, 4))

        g = nx.DiGraph()
        g.add_nodes_from(core.A)
        g.add_nodes_from(core.B)
        g.add_edges_from(P)

        color_map = []
        pos = {}
        i = 0
        j = 0
        for node in g:
            if node in core.A:
                i += 1
                pos[node] = (i, 2)
                color_map.append("blue")
            else:
                j += 1
                pos[node] = (j, 1)
                color_map.append("green")

        nx.draw(
            g,
            with_labels=True,
            node_size=2500,
            font_size=12,
            node_color=color_map,
            pos=pos,
        )
        plt.show()

    def mtr_rus_btn(self):
        """
        Drawing plot for SunionR!
        Not optimized plot generator
        """
        P = core.S.union(core.R)

        P = list(P)
        P.sort()

        plt.figure("Set S.union(R)", figsize=(8, 4))

        g = nx.DiGraph()
        g.add_nodes_from(core.A)
        g.add_nodes_from(core.B)
        g.add_edges_from(P)

        color_map = []
        pos = {}
        i = 0
        j = 0
        for node in g:
            if node in core.A:
                i += 1
                pos[node] = (i, 2)
                color_map.append("blue")
            else:
                j += 1
                pos[node] = (j, 1)
                color_map.append("green")

        nx.draw(
            g,
            with_labels=True,
            node_size=2500,
            font_size=12,
            node_color=color_map,
            pos=pos,
        )
        plt.show()

    def mtr_rds_btn(self):
        """
        Drawing plot for RintersectionS!
        Not optimized plot generator
        """
        P = core.R.intersection(core.S)

        P = list(P)
        P.sort()

        plt.figure("Set R.intersection(S)", figsize=(8, 4))

        g = nx.DiGraph()
        g.add_nodes_from(core.A)
        g.add_nodes_from(core.B)
        g.add_edges_from(P)

        color_map = []
        pos = {}
        i = 0
        j = 0
        for node in g:
            if node in core.A:
                i += 1
                pos[node] = (i, 2)
                color_map.append("blue")
            else:
                j += 1
                pos[node] = (j, 1)
                color_map.append("green")

        nx.draw(
            g,
            with_labels=True,
            node_size=2500,
            font_size=12,
            node_color=color_map,
            pos=pos,
        )
        plt.show()

    def mtr_rms_btn(self):
        """
        Drawing plot for RdifferenceS!
        Not optimized plot generator
        """
        P = core.R.difference(core.S)

        P = list(P)
        P.sort()

        plt.figure("Set R.difference(S)", figsize=(8, 4))

        g = nx.DiGraph()
        g.add_nodes_from(core.A)
        g.add_nodes_from(core.B)
        g.add_edges_from(P)

        color_map = []
        pos = {}
        i = 0
        j = 0
        for node in g:
            if node in core.A:
                i += 1
                pos[node] = (i, 2)
                color_map.append("blue")
            else:
                j += 1
                pos[node] = (j, 1)
                color_map.append("green")

        nx.draw(
            g,
            with_labels=True,
            node_size=2500,
            font_size=12,
            node_color=color_map,
            pos=pos,
        )
        plt.show()

    def mtr_umr_btn(self):
        """
        Drawing plot for UdifferenceS!
        Not optimized plot generator
        """
        U = set()
        for a in core.A:
            for b in core.B:
                U.add((a, b))
        P = U.difference(core.R)
        print(P)
        P = list(P)
        P.sort()

        plt.figure("Set U.difference(R)", figsize=(8, 4))

        g = nx.DiGraph()
        g.add_nodes_from(core.A)
        g.add_nodes_from(core.B)
        g.add_edges_from(P)

        color_map = []
        pos = {}
        i = 0
        j = 0
        for node in g:
            if node in core.A:
                i += 1
                pos[node] = (i, 2)
                color_map.append("blue")
            else:
                j += 1
                pos[node] = (j, 1)
                color_map.append("green")

        nx.draw(
            g,
            with_labels=True,
            node_size=2500,
            font_size=12,
            node_color=color_map,
            pos=pos,
        )
        plt.show()

    def mtr_st_btn(self):
        """
        Drawing plot for S ^ (-1)!
        Not optimized plot generator
        """
        Pl = core.S

        Pl = list(Pl)
        P = list()

        for l in Pl:
            P.append((l[1], l[0]))

        P.sort()

        plt.figure("Set S ^ (-1)", figsize=(8, 4))

        g = nx.DiGraph()
        g.add_nodes_from(core.A)
        g.add_nodes_from(core.B)
        g.add_edges_from(P)

        color_map = []
        pos = {}
        i = 0
        j = 0
        for node in g:
            if node in core.A:
                i += 1
                pos[node] = (i, 2)
                color_map.append("blue")
            else:
                j += 1
                pos[node] = (j, 1)
                color_map.append("green")

        nx.draw(
            g,
            with_labels=True,
            node_size=2500,
            font_size=12,
            node_color=color_map,
            pos=pos,
        )
        plt.show()

    def abt_btn(self):
        self.window = ab_iface.MyFormAbout()
        self.window.show()
