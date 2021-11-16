from settings import *

class Motor:
    def __init__(self, p1, p2, pm):
        self.pin1 = p1
        self.pin2 = p2
        self.pwm = pm
        self.m = None# GPIO.PWM(self.pin1, 50)
        #self.m.start(2)
        #GPIO.output(self.p1,True)
        #GPIO.output(self.p2, False)

    def adelante(self):
        #GPIO.output(self.p1,True)
        #GPIO.output(self.p2, False)
        print('adelante')

    def atras(self):
        #GPIO.output(self.p2,True)
        #GPIO.output(self.p1, False)
        print('atras')

    def stop(self):
        #GPIO.output(self.p1,False)
        #GPIO.output(self.p2, False)
        #GPIO.cleanup(self.p1)
        #GPIO.cleanup(self.p2)
        print('stop motor')

    def cambio(self, ang):
        base = 180.0
        pwm_ang = (ang/base)*10.0 + 2.0
        print("motor pwm {}".format(pwm_ang))
        if self.m != None:
            '''
            self.m.ChangeDutyCycle(pwm_ang)
            '''