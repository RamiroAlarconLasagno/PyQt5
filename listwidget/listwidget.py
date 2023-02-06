# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 17:16:47 2020

@author: ramir
"""

import sys 
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic

class Ventana(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("listwidget.ui", self)
        #*********Evento click**********
        self.Boton.clicked.connect(self.getItems)
        #Agregamos un nuevo item
        self.Lenguajes.addItem("C++")
        #Eliminar un item
        self.deleteItem("Python")
    #*********************Definimos funciones************************
    def getItems(self):
        items = self.Lenguajes.selectedItems()
        #Array para fuardar los items seleccionados
        selected = []
        for x in range(len(items)):
           selected.append(self.Lenguajes.selectedItems()[x].text())
        self.label_Lenguajes.setText("Seleccionados: "+ "-".join(selected))
    #***************************************************************** 
        '''Como solo se puede eliminar  por ubicacion, se hace un array de 
        las opciones, luego se recorre ese array comparando si existe la 
        opcion y su la encuentra la elimina.'''
    def deleteItem(self,label):
        #Array para almacenar cada item objeto
        items = []
		#Recorrer item a item
        for x in range(self.Lenguajes.count()):
             item = self.Lenguajes.item(x)
             items.append(item)
		#este array almacena el texto de cada item
        labels = [i.text() for i in items]
		#Recorrer item a item el array labels
        for x in range(len(labels)):
    		#Si el item existe
            if labels[x] == label:
				#Eliminar
                item = self.Lenguajes.indexFromItem(self.Lenguajes.item(x))
                self.Lenguajes.model().removeRow(item.row())
                
app = QApplication(sys.argv)
ventana = Ventana()
ventana.show()
app.exec_()