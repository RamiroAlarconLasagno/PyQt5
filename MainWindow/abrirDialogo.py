# -*- coding: utf-8 -*-
"""
Crearemos una ventana secundaria de main window

"""

import sys
from PyQt5.QtWidgets import QApplication , QMainWindow, QDialog, QPushButton, QLabel
from PyQt5 import uic
###############################################################################
class Dialogo (QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.resize(300,300)
        self.setWindowTitle("Cuadro de dialogos")
        self.etiqueta = QLabel(self)
        uic.loadUi("stylesheet.ui", self)
#*****************************************************************************        
class Ventana (QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(600,600)
        self.setWindowTitle("Ventana principal")
        self.boton = QPushButton(self)
        self.boton.setText("Abrir cuadro de dialogo")
        self.boton.resize(200,30)
        self.dialogo = Dialogo()
        self.boton.clicked.connect(self.abrirDialogo)
    #--------------------------------------------------------------------------    
    def abrirDialogo(self):
        self.dialogo.etiqueta.setText("Dialogo abierto desde la ventana principal")
        self.dialogo.exec_()
###############################################################################
app = QApplication(sys.argv)
ventana = Ventana()
ventana.show()
app.exec_()