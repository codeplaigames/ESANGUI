import time
#import RPi.GPIO as GPIO
from PyQt5.QtCore import QObject, pyqtSignal, Qt, QThread
from settings import *
import random


class Ultra(QThread):
    change_ultra_signal = pyqtSignal(int)
    def __init__(self, trig, echo, parent: QObject):
        super().__init__(parent)
        self.GPIO_TRIGGER = trig #16
        self.GPIO_ECHO    = echo #22
        self.run_flag = True

    def distance(self):
        time.sleep(1)
        # Send 10us pulse to trigger
        #GPIO.output(GPIO_TRIGGER, True)
        time.sleep(0.00001)
        #GPIO.output(GPIO_TRIGGER, False)
        start = time.time()

        #while GPIO.input(GPIO_ECHO)==0:
        start = time.time()

        #while GPIO.input(GPIO_ECHO)==1:
        stop = time.time()

        # Calculate pulse length
        elapsed = stop-start

        # Distance pulse travelled in that time is time
        # multiplied by the speed of sound (cm/s)
        distancet = elapsed * 34300

        # That was the distance there and back so halve the value
        distance = distancet / 2

        print  ("Distance :", distance, " cm")
        distance = random.randint(10,100)
        return distance
        
    def run(self):
        while self.run_flag:
            dist = self.distance()
            self.change_ultra_signal.emit(dist)
            time.sleep(1)

    def stop(self):
        self.run_flag = False
        #GPIO.cleanup(GPIO_TRIGGER)
        #GPIO.cleanup(GPIO_ECHO)
        self.wait()
# Set pins as output and input
#GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
#GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

# Set trigger to False (Low)
#GPIO.output(GPIO_TRIGGER, False)