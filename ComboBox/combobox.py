# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 16:48:16 2020

@author: ramir
"""

import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic

class Ventana(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("combobox.ui",self)
        #Funciones
        self.Boton.clicked.connect(self.getItem)
        #********Agregamos nuevo item******
        #self.Lenguaje.addItem("Ruby") #Agregamos un nuevo item.    
        #*******Eliminar un item***********
        self.Lenguaje.removeItem(0)
    #********Definimos funciones***********    
    def getItem(self):
        item = self.Lenguaje.currentText() #Tomo lo escrito en Lenguaje
        self.label_Lenguaje.setText("Has seleccionado: "+item)
#******************************************************************************  

app = QApplication(sys.argv)
ventana = Ventana()
ventana.show()
app.exec_() #ejecutar app