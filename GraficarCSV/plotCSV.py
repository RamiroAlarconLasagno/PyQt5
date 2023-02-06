# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys

# Importar librerias necesarias para crear la interfaz gráfica y trabajar con datos
import pandas as pd
from matplotlib import pyplot as plt
from PyQt5 import uic, QtWidgets

qtCreatorFile = "graficoCSV.ui" # Nombre del archivo que contiene la interfaz gráfica

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        # Conectar los botones con las funciones correspondientes
        self.boton1.clicked.connect(self.getCSV)
        self.boton2.clicked.connect(self.plot)
    
    def plot(self):
        x = self.df['col1']
        y = self.df['col2']
        plt.plot(x,y)
        plt.show(block=False)
        estad_st = "Estadisticas de col2: " + str(self.df['col2'].describe())
        self.resultado.setText(estad_st)
    
    def getCSV(self):
        try:
            filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 'C:/Users/ramir/OneDrive/Escritorio/Proyecto')
            if filePath != '':
                self.df = pd.read_csv(str(filePath))
        except Exception as e:
            print("Error:", e)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    app.exec_()