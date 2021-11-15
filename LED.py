from settings import *

class LED:
    def __init__(self, p):
        self.port = p
        GPIO.setup(self.port,GPIO.OUT)
        self.pw = True

    def power(self):
        GPIO.output(self.port, self.pw)
        self.pw = not self.pw 
        print("led : {}".format(self.pw))