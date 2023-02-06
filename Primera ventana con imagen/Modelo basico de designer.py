# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys

# Importar librerias necesarias para crear la interfaz gráfica
from PyQt5 import uic, QtWidgets

# Nombre del archivo que contiene la interfaz gráfica
qtCreatorFile = "Ventana.ui" 

# Cargar la interfaz gráfica desde el archivo especificado
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Inicializar la ventana principal
        QtWidgets.QMainWindow.__init__(self)
        # Inicializar la clase de la interfaz gráfica cargada
        Ui_MainWindow.__init__(self)
        # Configurar la interfaz gráfica y asociar elementos con métodos/atributos de la clase
        self.setupUi(self)
   
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show() # agregar parentesis para ejecutar el metodo show  
    app.exec_()
    
    