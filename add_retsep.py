from PyQt5.QtWidgets import *
from qeriy import Mysql

class AddWin(QWidget):
    def __init__(self,addwin):
        super().__init__()
        self.add = addwin

        self.data = Mysql()

        self.resize(500,600)
        self.setStyleSheet("font-size:20px")

        self.h_btn_lyt = QHBoxLayout()
        self.v_main_lyt = QVBoxLayout()

        self.btn_sub = QPushButton("Submit",clicked = self.submit)
        self.btn_sub.setFixedSize(200,80)
        self.btn_sub.setStyleSheet("background:skyblue")

        self.btn_back = QPushButton("Back",clicked = self.back)
        self.btn_back.setFixedSize(200,80)
        self.btn_back.setStyleSheet("background:skyblue")

        self.edit_name = QLineEdit()
        self.edit_name.setFixedSize(480,80)
        self.edit_name.setPlaceholderText("Taom nomini kiriting...")
        self.edit_maxsulot = QLineEdit()
        self.edit_maxsulot.setFixedSize(480,80)
        self.edit_maxsulot.setPlaceholderText("Maxsulotlarni kiriting...")
        self.edit_usul = QLineEdit()
        self.edit_usul.setFixedSize(480,80)
        self.edit_usul.setPlaceholderText("Tayyorlanish usulini kiriting...")

        self.lts_edit = [self.edit_name,self.edit_maxsulot,self.edit_usul]

        self.h_btn_lyt.addWidget(self.btn_sub)
        self.h_btn_lyt.addWidget(self.btn_back)

        self.v_main_lyt.addWidget(self.edit_name)
        self.v_main_lyt.addWidget(self.edit_maxsulot)
        self.v_main_lyt.addWidget(self.edit_usul)

        self.v_main_lyt.addLayout(self.h_btn_lyt)

        self.setLayout(self.v_main_lyt)

    def submit(self):
        for i in self.lts_edit:
            if not i.text():
                QMessageBox.warning(self,"Xato","Maydonni to'liq to'ldiring!!!")
                return
        temp = self.data.insert([i.text() for i in self.lts_edit])
        if temp:
            [i.clear() for i in self.lts_edit]
            QMessageBox.information(self,"Ajoyib","Malumotlar qo'shildi")
        else:
            QMessageBox.warning(self,"Xato","Xatolik yuz berdi")

    def back(self):
        self.add.show()
        self.hide()
