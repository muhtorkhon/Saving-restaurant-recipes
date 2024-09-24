from PyQt5.QtWidgets import *
from qeriy import Mysql
class Search(QWidget):
    def __init__(self,search):
        super().__init__()

        self.edit = search

        self.resize(500,600)
        self.setStyleSheet("font-size:20px")

        self.data = Mysql()

        self.h_btn_lyt = QHBoxLayout()
        self.v_main_lyt = QVBoxLayout()

        self.win_data = QTableWidget()
        
        self.btn_add = QPushButton("Search",clicked = self.delet)
        self.btn_add.setFixedSize(200,80)
        self.btn_add.setStyleSheet("background:skyblue")

        self.btn_edit = QPushButton("Back",clicked = self.backk)
        self.btn_edit.setFixedSize(200,80)
        self.btn_edit.setStyleSheet("background:skyblue")

        self.edit_del = QLineEdit()
        self.edit_del.setFixedSize(480,60)
        self.edit_del.setPlaceholderText("Taom nomini kiriting...")

        self.h_btn_lyt.addWidget(self.btn_add)
        self.h_btn_lyt.addWidget(self.btn_edit)

        self.v_main_lyt.addWidget(self.edit_del)
        self.v_main_lyt.addWidget(self.win_data)
        self.v_main_lyt.addLayout(self.h_btn_lyt)

        self.setLayout(self.v_main_lyt)


    def delet(self):
        temp = self.data.search_r(self.edit_del.text())
        if temp:
            self.win_data.setRowCount(len(temp))
            self.win_data.setColumnCount(4)
            for r_i, q in enumerate(temp):
                for c_i, u in enumerate(q):
                    self.win_data.setItem(r_i,c_i,QTableWidgetItem(str(u)))
            QMessageBox.information(self,"Ajoyib","Malumotlar taxrirlandi")
        else:
            QMessageBox.warning(self,"Xato","Xatolik yuz berdi")
    def backk(self):
        self.edit.show()
        self.hide()