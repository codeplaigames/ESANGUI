from PyQt5.QtCore import QObject, pyqtSignal, Qt, QThread
from settings import *
import time
import random

class Switch(QThread):
    
    change_val_signal = pyqtSignal(int)
    def __init__(self, port, caja, parent:QObject):
        super().__init__(parent)
        
        self.run_flag = True
        self.button = port
        self.texto = caja
        #GPIO.setup(port, GPIO.IN, GPIO.PUD_UP)
        print()

    def run(self):
        while self.run_flag:
            boton = random.randint(0,100) #GPIO.input(self.button)
            #self.texto.setText(str(boton))
            self.change_val_signal.emit(boton)
            time.sleep(0.5)

    def stop(self):
        self.run_flag = False
        #GPIO.cleanup(self.button)
        self.wait()