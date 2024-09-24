from PyQt5.QtWidgets import *
from add_retsep import AddWin
from delete_retsep import Delete
from edit_retsep import Edit
from search_retsep import Search
class MainWin(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(500,600)
        self.setStyleSheet("font-size:20px")



        self.h_btn_lyt = QHBoxLayout()
        self.v_main_lyt = QVBoxLayout()

        self.btn_add = QPushButton("Add retsept",clicked = self.addretsept)
        self.btn_add.setFixedSize(300,80)
        self.btn_add.setStyleSheet("background:skyblue")

        self.btn_edit = QPushButton("Editr retsept",clicked = self.editretsept)
        self.btn_edit.setFixedSize(300,80)
        self.btn_edit.setStyleSheet("background:skyblue")

        self.btn_del = QPushButton("Delete retsept",clicked = self.deletretsept)
        self.btn_del.setFixedSize(300,80)
        self.btn_del.setStyleSheet("background:skyblue")

        self.btn_search = QPushButton("Search retsept",clicked = self.searchretsept)
        self.btn_search.setFixedSize(300,80)
        self.btn_search.setStyleSheet("background:skyblue")

        self.btn_exit = QPushButton("Exit",clicked = exit)
        self.btn_exit.setFixedSize(300,80)
        self.btn_exit.setStyleSheet("background:skyblue")

        self.v_main_lyt.addWidget(self.btn_add)
        self.v_main_lyt.addWidget(self.btn_edit)
        self.v_main_lyt.addWidget(self.btn_del)
        self.v_main_lyt.addWidget(self.btn_search)
        self.v_main_lyt.addWidget(self.btn_exit)

        self.h_btn_lyt.addStretch()
        self.h_btn_lyt.addLayout(self.v_main_lyt)
        self.h_btn_lyt.addStretch()

        self.setLayout(self.h_btn_lyt)


    def addretsept(self):
        self.add = AddWin(self)
        self.add.show()
        self.hide()

    def editretsept(self):
        self.edit = Edit(self)
        self.edit.show()
        self.hide()

    def deletretsept(self):
        self.dellet = Delete(self)
        self.dellet.show()
        self.hide()

    def searchretsept(self):
        self.searchwin = Search(self)
        self.searchwin.show()
        self.hide()

  



    