# -*- coding: utf-8 -*-
"""
Validaremos formularios con expresiones regulares
"""

import sys, re #re valida
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5 import uic
#******************************************************************************
class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("validacion.ui",self)
        #Si cambia el texto aplicar esta funcion
        self.nombre.textChanged.connect(self.validar_nombre)
        self.email.textChanged.connect(self.validar_email)
        #Si hago click en este boton aplicar esta funcion
        self.boton_validar.clicked.connect(self.validar_formulario)
        
        #************Funsiones de validacion *****************
    def validar_nombre(self):
        nombre = self.nombre.text()
        validar = re.match('^[a-z\sáéíóúàèìòùäëïöüñ]+$',nombre, re.I) 
#Expresiones regulares para detectar nombres, acentos vocales, espacios,etc
        if nombre == "":
            self.nombre.setStyleSheet("border: 1px solid yellow;")
            return False
        elif not validar:
            self.nombre.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.nombre.setStyleSheet("border: 1px solid green;")
            return True
        
    def validar_email(self):
        email = self.email.text()
        validar = re.match('^[a-zA-Z0-9\._-]+@[a-zA-Z0-9-]{2,}[.][a-zA-Z]{2,4}$',email, re.I) 
#Expresiones regulares para detectar nombres, acentos vocales, espacios,etc
        if email == "":
            self.email.setStyleSheet("border: 1px solid yellow;")
            return False
        elif not validar:
            self.email.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.email.setStyleSheet("border: 1px solid green;")
            return True
    
    def validar_formulario(self):
        if self.validar_nombre() and self.validar_email():
            QMessageBox.information(self, "Formulario correcto", 
                                    "Validación correcta", QMessageBox.Discard) 
            #Boton discard de aceptar
        else:
            QMessageBox.information(self, "Formulario incorrecto", 
                                    "Validación incorrecta",QMessageBox.Discard)            
#******************************************************************************
            
app = QApplication(sys.argv)
dialogo = Dialogo()
dialogo.show()
app.exec_()
            
            
            
            