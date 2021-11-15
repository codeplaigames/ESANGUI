from settings import *

class Servo:
    def __init__(self, id):
        self.pin = id
        #GPIO.setup(self.servo1_pin, GPIO.OUT)
        self.servo = None #GPIO.PWM(self.servo1_pin,50)
        #self.servo.start(7.5)
    def change_ang(self, ang):
        base = 180.0
        pwm_ang = (ang/base)*10.0 + 2.0
        if (self.servo!= None):
            '''
            self.servo.ChangeDutyCycle(pwm_ang)
            '''
        
    def stopped(self):
        #self.servo.stop()
        #GPIO.cleanup(self.id)
        print()