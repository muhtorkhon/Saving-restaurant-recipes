from PyQt5.QtWidgets import *
from qeriy import Mysql
class Edit(QWidget):
    def __init__(self,edit):
        super().__init__()

        self.edit = edit

        self.resize(500,600)
        self.setStyleSheet("font-size:20px")

        self.data = Mysql()

        self.h_btn_lyt = QHBoxLayout()
        self.v_main_lyt = QVBoxLayout()

        self.wedit = QTableWidget()
        temp = self.data.all_data()
        self.wedit.setRowCount(len(temp))
        self.wedit.setColumnCount(4)
        for row_i, row_data in enumerate(temp):
            for col_i, col_data in enumerate(row_data):
                self.wedit.setItem(row_i, col_i, QTableWidgetItem(str(col_data)))
        


        self.btn_add = QPushButton("Update",clicked = self.delet)
        self.btn_add.setFixedSize(200,80)
        self.btn_add.setStyleSheet("background:skyblue")

        self.btn_edit = QPushButton("Back",clicked = self.backk)
        self.btn_edit.setFixedSize(200,80)
        self.btn_edit.setStyleSheet("background:skyblue")

        self.h_btn_lyt.addWidget(self.btn_add)
        self.h_btn_lyt.addWidget(self.btn_edit)

        self.v_main_lyt.addWidget(self.wedit)
        self.v_main_lyt.addLayout(self.h_btn_lyt)

        self.setLayout(self.v_main_lyt)


    def delet(self):
        current_row = self.wedit.currentRow()
        row_id = int(self.wedit.item(current_row, 0).text())
        new_name = self.wedit.item(current_row, 1).text()
        new_maxsulot = self.wedit.item(current_row, 2).text()
        new_usuli = self.wedit.item(current_row, 3).text()
    
        temp = self.data.update(row_id, new_name, new_maxsulot, new_usuli)
        if temp:
            QMessageBox.information(self,"Ajoyib","Malumotlar taxrirlandi")
        else:
            QMessageBox.warning(self,"Xato","Xatolik yuz berdi")
    def backk(self):
        self.edit.show()
        self.hide()