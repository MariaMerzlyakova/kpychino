import sys
import sqlite3
from PyQt5.QtGui import QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()
        self.pushButton.clicked.connect(self.se)
        self.pushButton_2.clicked.connect(self.kk)
        self.search()
 
    def search(self):
        queue = f"SELECT * FROM k WHERE ID != ''"
        res = self.cur.execute(queue).fetchall()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'название сорта', 'степень обжарки',
                                          'молотый/в зернах', 'описание вкуса', 'цена', 'объем упаковки'])
        if res:
            self.tableWidget.setRowCount(len(res))
            self.tableWidget.setColumnCount(len(res[0]))
            for i, elem in enumerate(res):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
    def se(self):
        self.w = MyWidget2()
        self.w.show()

    def kk(self):
        self.search()
        

class MyWidget2(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.pushButton.clicked.connect(self.s)

    def s(self):
        a = self.lineEdit_2.text()
        b = self.lineEdit_3.text()
        c = self.lineEdit_4.text()
        d = self.lineEdit_5.text()
        e = self.lineEdit_6.text()
        f = self.lineEdit_7.text()
        
        m = sqlite3.connect('coffee.sqlite')
        rrr = m.cursor()
        print(111)
        itog = rrr.execute('''SELECT * FROM k WHERE ID = ?''', (self.lineEdit.text(),)).fetchall()
        print(666)
        if itog:
            rrr.execute("""UPDATE k
                     SET a = ?, b = ?, c = ?, d = ?, e = ?, f = ?
                    WHERE ID = ?""", (a, b, c, d, e, f, self.lineEdit.text(),))
        else:
            rrr.execute("""INSERT INTO k(ID, a, b, c, d, e, f) VALUES(?,?,?,?,?,?,?)""", (self.lineEdit.text(), a, b, c, d, e, f,))
            
        m.commit()
        m.close()
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
