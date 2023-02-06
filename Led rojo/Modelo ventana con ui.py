# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 12:51:53 2023

@author: ramir
"""
# Importar librerias necesarias para crear la interfaz gráfica
from PyQt5 import QtWidgets
import sys
from PyQt5 import uic

# Nombre del archivo que contiene la interfaz gráfica
qtCreatorFile = "Led Rojo.ui" 

# Cargar la interfaz gráfica desde el archivo especificado
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile) 

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Inicializar la ventana principal
        super().__init__()
        # Configurar la interfaz gráfica y asociar elementos con métodos/atributos de la clase
        self.setupUi(self)
        self.radioButton.setDisabled(True) # deshabilitar radioButton
        self.pushButton.clicked.connect(lambda: self.cambio())  
        
    def cambio(self):
        print(self.radioButton.isChecked())
        self.radioButton.setEnabled(True) # Habilitar radioButton
        self.radioButton.setChecked(not self.radioButton.isChecked()) # Cambia el valor de radioButton
        self.radioButton.setDisabled(True) # Desabilitar radioButton
            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    app.exec_()
