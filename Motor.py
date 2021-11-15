from settings import *

class Motor:
    def __init__(self, pm,p1, p2):
        self.pin1 = p1
        self.pin2 = p2
        self.pwm = pm
        GPIO.setup(self.pwm, GPIO.OUT)
        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)
        self.m = GPIO.PWM(self.pwm, 50)
        self.m.start(0)
        GPIO.output(self.pin1,False)
        GPIO.output(self.pin2, False)

    def adelante(self):
        GPIO.output(self.pin1,True)
        GPIO.output(self.pin2, False)
        print('adelante')

    def atras(self):
        GPIO.output(self.pin2,True)
        GPIO.output(self.pin1, False)
        print('atras')

    def stop(self):
        GPIO.output(self.pin1,False)
        GPIO.output(self.pin2, False)
        #GPIO.cleanup(self.pin1)
        #GPIO.cleanup(self.pin2)
        #self.m.stop()
        print('stop motor')

    def cambio(self, ang):
        print("cambio motor: {}".format(ang))
        if self.m != None:
            self.m.ChangeDutyCycle(ang)