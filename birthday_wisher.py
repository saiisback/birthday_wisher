from datetime import date 
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtWidgets


today = date.today()
day = today.day
month = today.month

birthday = [['sai' , 24 , 12], ['vidhu',6,3 ]]

for i in birthday:
    if i[1] == today.day and i[2] == today.month :
        birthday_person = i[0]
    else:
        pass


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 787)
        MainWindow.setWindowTitle("Birthday wisher")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(0, 0, 1400, 787)
        self.label.setText("")
        self.label.setPixmap(QPixmap("main_background.jpg"))
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(360, 410 ,750, 100)
        self.label_1.setText(f"Today is {birthday_person}'s birthday")
        self.label_1.setObjectName("label1")
        self.label_1.setStyleSheet("background-color:white;border-radius:10%;font-size: 60px;font-weight: bold;color: black")
       
        MainWindow.setCentralWidget(self.centralwidget)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
