# -*- coding: utf-8 -*-
"""
Creamos un navegador.
Con el boton back se retrocede a una pagina anterior en el historial
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import uic

class Navegador(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("webkit.ui", self)
        self.navegador = QWebEngineView()
        #URL por defecto
        default_url = "http://google.com"
        #Navegar a la url por defecto
        self.navegador.load(QUrl(default_url))
        #Agregar al buscador la url por defecto
        self.url.setText(default_url)
        #Desactivar boton backhasta que no haya historial
        self.btn_back.setEnabled(False)
        
        #retrocedemos a la pagina anterior
        self.btn_back.clicked.connect(self.navegador.back)
        self.url.returnPressed.connect(self.navegar)#se activa cuando apretas enter en return
        self.navegador.urlChanged.connect(self.url_changed)
    #******************Definimos metodos*************************
    #PPara navegar a la url indicada en el buscador al presionar enter
    def navegar(self):
        url = QUrl(self.url.text())#Copiar la direccion de url.text
        self.navegador.setUrl(url)#Ir a esa direccion
    #Detectar el cambio de url de navegacion
    def url_changed(self):
        #Creamos un objeto de la pagina.
        page = self.navegador.page()
        history = page.history()
        #Si hay historial activar el boton back
        if history.canGoBack():
            self.btn_back.setEnabled(True)
        else:
            self.btn_back.setEnabled(False)
        #Agregar el cambio de url al campo de busqueda
        url = self.navegador.url()
        self.url.setText(url.toString())
#******************************************************************************
app = QApplication(sys.argv)
navegador = Navegador()
navegador.show()
app.exec_()
