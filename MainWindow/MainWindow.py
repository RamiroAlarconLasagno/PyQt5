# -*- coding: utf-8 -*-
"""
Vamos a intentar crear nuestra primera ventana usando pyqt
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic #Para manejar archibos.uic
#Cambiar tipo de fuente o letra
from PyQt5.QtGui import QFont
# Modificar el cursor
from PyQt5.QtCore import Qt
#Nos permite obtener tanto el ancho como el alto del escritorio
import ctypes #GetSystemMetrics

###############################################################################

#Clase heredada de QMainWindow (Constructor de ventanas)
class Ventana(QMainWindow):
    #Método constructor de la clase
    def __init__(self):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self) #dentro de ventana se ejecuta el metodo de QMainWindow
        #Cargar la configuración del archivo .ui en el objeto
        uic.loadUi("MainWindow.ui", self)
        
        #*********************Funciones de ventana*************************
        self.setWindowTitle("Nombre de la ventana")
        #Mostrar la ventana maximizada
        self.showMaximized()
        #Fijar el tamaño minimo de la ventana
        self.setMinimumSize(500,500)
        #fijar el tamaño maximo
        self.setMaximumSize(500,500)
        #Mover la ventana y centrarla en el escritorio
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)
        left = (resolucion_ancho / 2) - (self.frameSize().width() / 2)
        top = (resolucion_alto / 2) - (self.frameSize().height() / 2)
        self.move(left, top)
        #Desactivar la ventana y sus elementos internos.
        #self.setEnabled(False)
        #Asignaremos un tipo especifico de fuente.
        qfont = QFont("Cambria Math", 12, QFont.Bold)
        self.setFont(qfont)
        #Asignar un tipo de cursor
        self.setCursor(Qt.PointingHandCursor)
        #Asignar estilos CSS
        #self.setStyleSheet("background-color: #000; color:#fff;")
        #---Asignarle propiedades al boton de nombre pushButtonBoton
        self.pushButtonBoton.setStyleSheet("background-color:#000;color:#fff; font-size:14px")
    #--------------------------------------------------------------------------
       #Definimos un evento que se genera cuando se crea la ventana
    def showEvent(self, event):
       self.Bienvenido.setText("!!!Bienvenidooooo!!!")
    #--------------------------------------------------------------------------
       #Evento para cuando se cierra la ventana
    def closeEvent(self, event):
        resultado = QMessageBox.question(self, "Salir", "Seguro que quieres salir?",
                                QMessageBox.Yes|QMessageBox.No)
        if resultado == QMessageBox.Yes: event.acept()
        else: event.ignore()
    #--------------------------------------------------------------------------
       #Evento para cuando movemos la ventana.
    def moveEvent(self, event):
        x = str(event.pos().x())
        y = str(event.pos().y())
        self.Posicion.setText("x: "+ x +"y: "+ y)
###############################################################################
#Instancia para iniciar una aplicación
app = QApplication(sys.argv) #Argumentos obligatorios
#Crear un objeto de la clase
_ventana = Ventana()
#Mostra la ventana
_ventana.show()
#Ejecutar la aplicación
app.exec_()