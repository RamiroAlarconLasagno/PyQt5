# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 0, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.calendario = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendario.setGeometry(QtCore.QRect(60, 80, 671, 261))
        self.calendario.setStyleSheet("background-color: rgb(255, 170, 0)")
        self.calendario.setObjectName("calendario")
        self.Op1 = QtWidgets.QCheckBox(self.centralwidget)
        self.Op1.setGeometry(QtCore.QRect(130, 380, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Op1.setFont(font)
        self.Op1.setObjectName("Op1")
        self.Op2 = QtWidgets.QCheckBox(self.centralwidget)
        self.Op2.setGeometry(QtCore.QRect(130, 430, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Op2.setFont(font)
        self.Op2.setObjectName("Op2")
        self.Imagen = QtWidgets.QLabel(self.centralwidget)
        self.Imagen.setGeometry(QtCore.QRect(410, 390, 301, 141))
        self.Imagen.setText("")
        self.Imagen.setPixmap(QtGui.QPixmap(":/Imagen/300px-OpticalSetupDHM.jpg"))
        self.Imagen.setObjectName("Imagen")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic; text-decoration: underline;\">Hola mundo</span></p></body></html>"))
        self.Op1.setText(_translate("MainWindow", "Opcion 1"))
        self.Op2.setText(_translate("MainWindow", "Opcion 2"))
import Imagen_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())