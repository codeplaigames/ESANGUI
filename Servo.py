from settings import *

class Servo:
    def __init__(self, id):
        self.pin = id
        GPIO.setup(self.pin, GPIO.OUT)
        self.servo = GPIO.PWM(self.pin,50)
        self.servo.start(2.0)
    def change_ang(self, ang):
        base = 180.0
        pwm_ang = (ang/base)*10.0 + 2.0
        print('angulo: {}'.format(pwm_ang))
        if (self.servo!= None):
            self.servo.ChangeDutyCycle(pwm_ang)
        
    def stopped(self):
        self.servo.stop()
        GPIO.cleanup(self.pin)
        print('Stop servo')