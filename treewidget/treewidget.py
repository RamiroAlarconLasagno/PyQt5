# -*- coding: utf-8 -*-
"""
Intentaremos emular una carpeta de busqueda:
"""

import sys, time
from PyQt5.QtWidgets import QApplication, QDialog, QTreeWidgetItem
from PyQt5 import uic
from os import listdir, path, stat, startfile #startfile abre archivos
from mimetypes import MimeTypes

class Buscador(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("treewidget.ui", self)
        self.boton_Buscar.clicked.connect(self.getDir)
        self.Directorio.itemDoubleClicked.connect(self.openElement)
    #******* definimos los metodos**************    
    def getDir(self):
        #Eliminar todas las filas de las busquedas anteriores
        self.Directorio.clear()
        #Ruta indicada por el usuario
        dir = self.Ruta.text()
        if path.isdir(dir):
            #Recorrer sus elementos
            for element in listdir(dir):
                name = element
                pathinfo = dir + "\\" + name
                informacion = stat(pathinfo)
                #Si es un directorio
                if path.isdir(pathinfo):
                    type = "Carpeta de archivos."
                    size = ""
                else: 
                    mime = MimeTypes()
                    type = mime.guess_type(pathinfo)[0]
                    size = str(informacion.st_size) + " [bytes]"
                #Fecha de modificacion
                date = str(time.ctime(informacion.st_mtime))
                #Crear un array para crear la fila con los items
                row = [name,date,type,size]
                #Insertar fila
                self.Directorio.insertTopLevelItems(0, [QTreeWidgetItem(self.Directorio, row)])
    #**************************************************************************
    def openElement(self): 
        #Obtener el item seleccionado por el usuario cuando haga doble click
        item = self.Directorio.currentItem()
        #Creamos la ruta accediendo al nombre del elemento (carpeta o archivo)
        elemento = self.Ruta.text() + "\\" +item.text(0)
        #Verifica si es un directorio y de ser asi navega en su interior
        if path.isdir(elemento):
            self.Ruta.setText(elemento)
            self.getDir()#Ir a esa direccion
        else: #De no ser un directorio (es un archivo)
            startfile(elemento)
            
        
app = QApplication(sys.argv)
buscador = Buscador()
buscador.show()
app.exec_()
