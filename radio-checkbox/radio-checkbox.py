# -*- coding: utf-8 -*-
"""
Aprendemos a usar botones radio y checkbox
"""
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic
#******************************************************************************
class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("radio-checkbox.ui", self)
        #Funciones de radio
        self.radio_value()# Se ejecuta una vez
        self.boton.clicked.connect(self.radio_value) #Cada vez que se toca el boton
        #Funciones de terminos
        self.estado_checkbox()
        self.boton.clicked.connect(self.estado_checkbox)
    #******** Defino funciones ******************
    def radio_value(self):
        if self.Python.isChecked():
            self.label_Lenguaje.setText("Python ha sido seleccionado")
        elif self.PHP.isChecked():
            self.label_Lenguaje.setText("PHP ha sido seleccionado")
        elif self.Perl.isChecked():
            self.label_Lenguaje.setText("Perl ha sido seleccionado")
        elif self.Ruby.isChecked():
            self.label_Lenguaje.setText("Ruby ha sido seleccionado")
        else:
            self.label_Lenguaje.setText("No hay seleccionado ningun lenguaje")
    #*******************************************
    def estado_checkbox(self):
        if self.Terminos.isChecked():
            self.label_Terminos.setText("Has aceptado los terminos")
        else:
            self.label_Terminos.setText("No has aceptado los terminos")
#******************************************************************************
app = QApplication(sys.argv)
dialogo = Dialogo()
dialogo.show()
app.exec_()