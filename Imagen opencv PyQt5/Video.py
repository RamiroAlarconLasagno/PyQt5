# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 15:13:08 2023

@author: ramir
"""
from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi 
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage, QPixmap
import imutils
import cv2
import sys

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        loadUi('design.ui', self)
		
        self.open_image.clicked.connect(self.inicio)
        self.reset_edit.clicked.connect(self.reset_image)

        self.filename = str() 

    def reset_image(self):
        self.grabar = False

    
    def inicio(self):
        self.grabar = True
        self.load_image()
        
    def load_image(self):
        camara_numero = 0
        cap = cv2.VideoCapture(camara_numero,cv2.CAP_DSHOW)
        Leido, imagen = cap.read()
        while self.grabar == True:
            # Leer un frame de la cámara
            ret, self.image = cap.read()
            self.hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
            image = cv2.cvtColor(self.hsv, cv2.COLOR_HSV2RGB)
            #image = cv2.flip(image, 1)
            frame = imutils.resize(image, width=800, height=800)
            image = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
            self.label_image.setPixmap(QPixmap.fromImage(image))	
            QtWidgets.QApplication.processEvents()
            if (self.grabar == False):
                cap.release()
                break          
        if self.grabar == False:
            cap.release()
                
    
    def closeEvent(self,event):
        result = QtWidgets.QMessageBox.warning(self,
                 "Confirm Exit...",
                 "Asegurese de haber cerrado el proceso antes de salir para evitar problemas con el cierre de la camara",
                 QtWidgets.QMessageBox.Yes| QtWidgets.QMessageBox.No)
        event.ignore()
        if result == QtWidgets.QMessageBox.Yes:
            self.reset_image()
            self.close()
            event.accept()    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec_())