import os
import subprocess
import time
import cv2
import sys

class Detect:
    def __init__(self, opc, caminho):
        self.opc = opc
        self.caminho = caminho
    
    def play(self):
        if self.opc == 25:
            carregar_img = cv2.imread(self.caminho)
            detector_face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            imagem_cinza = cv2.cvtColor(carregar_img, cv2.COLOR_BGR2GRAY)
            faces = detector_face.detectMultiScale(imagem_cinza, scaleFactor=1.01,minNeighbors=5, maxSize=(45, 45))
            for (x, y, w, h) in faces:
            	cv2.rectangle(carregar_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            	
            cv2.imshow('Rostos detectados', carregar_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            



opc = int(sys.argv[1])
caminho = sys.argv[2]
Detect(opc, caminho).play()
