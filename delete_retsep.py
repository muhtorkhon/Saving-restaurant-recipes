from PyQt5.QtWidgets import *
from qeriy import Mysql
class Delete(QWidget):
    def __init__(self,dell):
        super().__init__()

        self.dell = dell

        self.resize(500,600)
        self.setStyleSheet("font-size:20px")

        self.data = Mysql()

        self.h_btn_lyt = QHBoxLayout()
        self.v_main_lyt = QVBoxLayout()

        self.btn_add = QPushButton("Delete",clicked = self.delet)
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
        self.v_main_lyt.addLayout(self.h_btn_lyt)

        self.setLayout(self.v_main_lyt)


    def delet(self):
        temp = self.data.drop_data(self.edit_del.text())
        if temp:
            self.edit_del.clear()
            QMessageBox.information(self,"Ajoyib","Malumotlar o'chirildi")
        else:
            QMessageBox.warning(self,"Xato","Xatolik yuz berdi")
    def backk(self):
        self.dell.show()
        self.hide()