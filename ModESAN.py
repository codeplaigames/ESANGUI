import sys
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui
from LED import LED
from Motor import Motor
from Servo import Servo
from Switch import Switch
from Ultra import Ultra
from VideoThread import *
from MplCanvas import *
from mpu60 import *

from settings import *

class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Modulos GUI')
        self.setMinimumSize(1024,700)
        self.add_groups()
        self.camera()
        self.mpu()

    def loadPuertos(self):
        print()

    def add_groups(self):
        layout = QGridLayout()
        

        self.grupo1 = QGroupBox("Camara")
        self.grupo2 = QGroupBox("Sensores y actuadores")
       

        layout.addWidget(self.grupo1,0,0)
        layout.addWidget(self.grupo2,0,1)
        

        self.setLayout(layout)

    def ENA_LED1(self):
        print("led 1: ",end=" ")
        self.LD1.power()

    def ENA_LED2(self):
        print("led 1: ",end=" ")
        self.LD2.power()

    def ENA_LED3(self):
        print("led 1: ",end=" ")
        self.LD3.power()

  
    def ENA_LED4(self):
        print("led 1: ",end=" ")
        self.LD4.power()
        
    @pyqtSlot(np.ndarray)
    def mpu_values(self, datos):
        print("mpu valores: {}".format(datos))
        self.valores_mpu(datos)

    def activar_mpu(self):
        if self.mpuobj != None:
            self.mpuobj.start()
            self.bmpu.setEnabled(False)


    def mpu(self):
        hbox = QHBoxLayout()
        self.bmpu = QPushButton("On",self)
        self.bmpu.clicked.connect(self.activar_mpu)
        self.mpuobj = mpu60(self)
        self.mpuobj.cambio_senhal.connect(self.mpu_values)
        #self.mpuobj.MPU_Init()

        labelports = QLabel("MPU",self)
        hbox.addWidget(labelports)
        hbox.addWidget(self.bmpu)
        hbox.addStretch()

        principal = QVBoxLayout()
        principal.addLayout(hbox)

        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        self.sc.axes.plot([0,1,2,3,4], [-1,1,-1,0,0])
        principal.addWidget(self.sc)

        hboxmpu = QHBoxLayout()
        hboxmpu.addWidget(QLabel("ax"))
        hboxmpu.addWidget(QLabel("ay"))
        hboxmpu.addWidget(QLabel("ax"))
        hboxmpu.addWidget(QLabel("ang x"))
        hboxmpu.addWidget(QLabel("ang y"))
        hboxmpu.addWidget(QLabel("ang z"))

        principal.addLayout(hboxmpu)

        hb2 = QHBoxLayout()
        self.ax = QLabel("0")
        self.ay = QLabel("0")
        self.az= QLabel("0")
        self.angx = QLabel("0")
        self.angy = QLabel("0")
        self.angz= QLabel("0")

        hb2.addWidget(self.ax)
        hb2.addWidget(self.ay)
        hb2.addWidget(self.az)
        hb2.addWidget(self.angx)
        hb2.addWidget(self.angy)
        hb2.addWidget(self.angz)

        principal.addLayout(hb2)
        #ultrasonido switch
        sensorsrow = QHBoxLayout()
        sensorsrow.addWidget(QLabel("Ultrasonido"))
        self.bultra = QPushButton("On",self)
        self.sultra = Ultra(16,22, self)
        self.sultra.change_ultra_signal.connect(self.ultra_sonidos)
        self.bultra.clicked.connect(self.valor_ultra)
        

        sensorsrow.addWidget(self.bultra)
        self.tultra = QLineEdit()
        self.tultra.setText("0")
        self.tultra.setEnabled(False)
        sensorsrow.addWidget(self.tultra)
        sensorsrow.addSpacing(20)
        sensorsrow.addWidget(QLabel("Switch"))
        self.tswitch = QLineEdit()
        self.tswitch.setText("0")
        self.tswitch.setEnabled(False)
        #switch
        self.btactile = Switch(18, self.tswitch, self)
        self.btactile.start()
        self.btactile.change_val_signal.connect(self.get_tactile)

        sensorsrow.addWidget(self.tswitch)
        principal.addSpacing(20)
        principal.addLayout(sensorsrow)
        principal.addSpacing(20)
        principal.addWidget(QLabel("Leds"))

        #add leds row
        self.led1 = QPushButton("Led 1")
        self.led2 = QPushButton("Led 2")
        self.led3 = QPushButton("Led 3")
        self.led4 = QPushButton("Led 4")
        self.LD1 = LED(11)
        self.LD2 = LED(13)
        self.LD3 = LED(15)
        self.LD4 = LED(36)

        self.led1.clicked.connect(self.ENA_LED1)
        self.led2.clicked.connect(self.ENA_LED2)
        self.led3.clicked.connect(self.ENA_LED3)
        self.led4.clicked.connect(self.ENA_LED4)

        rleds = QHBoxLayout()
        rleds.addWidget(self.led1)
        rleds.addWidget(self.led2)
        rleds.addWidget(self.led3)
        rleds.addWidget(self.led4)

        principal.addLayout(rleds)

        #add servo control
        rservo = QHBoxLayout()
        rservo.addWidget(QLabel("Servo"))
        self.servoSolo = QPushButton("On")
        rservo.addWidget(self.servoSolo)
        self.objservoSolo = None
        self.servoSolo.clicked.connect(self.en_servo_solo)

        self.vservo = QLabel("[0]")
        rservo.addWidget(self.vservo)
        self.servoslider = QSlider(Qt.Horizontal, self)
        self.servoslider.setMinimum(0)
        self.servoslider.setMaximum(180)
        self.servoslider.setValue(0)
        self.servoslider.valueChanged.connect(self.cambio_servo_solo)

        rservo.addWidget(self.servoslider)
        principal.addSpacing(20)
        principal.addWidget(QLabel("Servo"))
        principal.addLayout(rservo)

        # add motor control
        rmotor = QHBoxLayout()
        rmotor.addWidget(QLabel("Dirección: "))
        self.badelante = QPushButton("Adelante")
        self.badelante.clicked.connect(self.enadelante)
        self.batras = QPushButton("Atras")
        self.batras.clicked.connect(self.enatras)
        self.vmotor = QLabel("0")
        self.pmotor = Motor(35,37,33)
        rmotor.addWidget(self.badelante)
        rmotor.addWidget(self.batras)
        self.bmotor_stop = QPushButton("Stop")
        self.bmotor_stop.clicked.connect(self.pmotor.stop)
        rmotor.addWidget(self.bmotor_stop)
        rmotor.addSpacing(20)
        rmotor.addWidget(self.vmotor)
        #slide motor
        self.motslider = QSlider(Qt.Horizontal, self)
        self.motslider.setMinimum(0)
        self.motslider.setMaximum(100)
        self.motslider.setValue(0)
        self.motslider.valueChanged.connect(self.cambio_motor)
        
        principal.addSpacing(20)
        principal.addWidget(QLabel("Motor"))
        principal.addLayout(rmotor)
        principal.addWidget(self.motslider)


        principal.addStretch()


        self.grupo2.setLayout(principal)

    def enadelante(self):
        self.pmotor.adelante()

    def enatras(self):
        self.pmotor.atras()

    def cambio_motor(self, valor):
        self.pmotor.cambio(valor)


    def en_servo_solo(self):
        if(self.objservoSolo == None):
            self.objservoSolo = Servo(31)
        else:
            self.objservoSolo.stopped()
            self.objservoSolo = None


    def cambio_servo_solo(self, val):
        if(self.objservoSolo != None):
            self.vservo.setText("["+str(val)+"]")
            self.objservoSolo.change_ang(val)

    def valor_ultra(self):
        if self.sultra != None:
            self.sultra.start()
            self.bultra.setEnabled(False)
        
    @pyqtSlot(float)
    def ultra_sonidos(self, dist):
        self.tultra.setText("{:.2f}".format(dist))

    def valores_mpu(self, vMPU):
        if (self.mpuobj != None):
            vMPU = vMPU.tolist()
            self.sc.drawio(vMPU)
            self.ax.setText("{:.2f}".format(vMPU[0]))
            self.ay.setText("{:.2f}".format(vMPU[1]))
            self.az.setText("{:.2f}".format(vMPU[2]))
            self.angx.setText("{:.2f}".format(vMPU[3]))
            self.angy.setText("{:.2f}".format(vMPU[4]))
            self.angz.setText("{:.2f}".format(vMPU[5]))


    def camera(self):
        hbox = QHBoxLayout()
        self.pcam = QPushButton("On",self)
        labelports = QLabel("Puertos",self)
        self.lports = QComboBox(self) #port list
        self.setWindowTitle("Qt live label demo")
        self.display_width = 640
        self.display_height = 480
        # create the label that holds the image
        self.image_label = QLabel(self)
        self.image_label.resize(self.display_width, self.display_height)

        # getting available cameras
        self.available_cameras = QCameraInfo.availableCameras()
        self.lports.addItems([camera.description() for camera in self.available_cameras])

        hboxcam = QHBoxLayout()
        hboxcam.addWidget(self.pcam)
        hboxcam.addWidget(labelports)
        hboxcam.addWidget(self.lports)
        #add space
        hboxcam.addSpacing(20)
        #add boton slider1
        self.bslider1 = QPushButton("On servo1")
        self.bslider1.clicked.connect(self.sliderservo1Act)
        self.bslider2 = QPushButton("On servo2")
        self.bslider2.clicked.connect(self.sliderservo2Act)
        hboxcam.addWidget(self.bslider1)
        hboxcam.addWidget(self.bslider2)

        hboxcam.addStretch()


        vboxcam = QVBoxLayout()
        vboxcam.addLayout(hboxcam)
        #camera slider

        camlayout =  QHBoxLayout()
        camlayout.addWidget(self.image_label)
        #slides
        sliderlayout = QVBoxLayout()
        sliderlayout.addWidget(QLabel("Eje 1"))
        self.ang_eje1 = QLabel("0")
        self.slider1 = QSlider(Qt.Vertical, self)
        self.slider1.setMinimum(0)
        self.slider1.setMaximum(180)
        self.slider1.setValue(0)
        self.slider1.setEnabled(False)
        self.slider1.valueChanged.connect(self.slider1cambio)
        #enlazar a funcion para que cambie

        #add to layout
        sliderlayout.addWidget(self.ang_eje1)
        sliderlayout.addWidget(self.slider1)

        camlayout.addLayout(sliderlayout)

        vboxcam.addLayout(camlayout)

        #las arrow 
        lrow = QHBoxLayout()
        lrow.addWidget(QLabel("Eje 2"))
        self.ang_eje2 = QLabel("0")
        lrow.addWidget(self.ang_eje2)
        self.slider2 = QSlider(Qt.Horizontal, self)
        self.slider2.setValue(0)
        self.slider2.setMinimum(0)
        self.slider2.setMaximum(180)
        self.slider2.setEnabled(False)
        self.slider2.valueChanged.connect(self.slider2cambio)
        lrow.addWidget(self.slider2)
        vboxcam.addLayout(lrow)

        self.grupo1.setLayout(vboxcam)
        
        #accion para iniciar camara
        #camera_action = QAction("Play", self)
        #camera_action.triggered.connect(self.oncamera)
        
        
        self.thread = None
        self.pcam.clicked.connect(self.oncamera)

        #vbox = QVBoxLayout()
        #vbox.addLayout(hbox)

        #servos connections
        self.servo1 = None
        self.servo1_pin = 32
        self.servo2 = None
        self.servo2_pin = 29
        
    

    def oncamera(self):
        puertoidx = self.lports.currentIndex()
        if( self.thread == None):
            print("Ingreso camara")
            self.pcam.setText("Off")
            # create the video capture thread
            self.thread = VideoThread(puertoidx)
            # connect its signal to the update_image slot
            self.thread.change_pixmap_signal.connect(self.update_image)
            # start the thread
            self.thread.start()
        else:
            self.thread.stop()
            self.thread = None
            self.pcam.setText("On")
    
    def closeEvent(self, event):
        if(self.thread != None):
            self.thread.stop()
            self.btactile.stop()
            self.sultra.stop()
            self.mpuobj.stop()
            GPIO.cleanup()
        event.accept()

    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.image_label.setPixmap(qt_img)
    
    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.display_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)

    @pyqtSlot(int)
    def get_tactile(self, boton):
        #print("recibio {}".format(boton))
        self.tswitch.setText(str(boton))

    def slider1cambio(self, value):
        self.ang_eje1.setText(str(value))
        if (self.servo1 != None):
            '''
            self.servo1.ChangeDutyCycle(pwm_ang)
            '''
            self.servo1.change_ang(value)


    def slider2cambio(self, value):
        self.ang_eje2.setText(str(value))
        if (self.servo2!= None):
            '''
            self.servo2.ChangeDutyCycle(pwm_ang)
            '''
            self.servo2.change_ang(value)

    def sliderservo1Act(self):
        if (self.servo1 == None):
            self.bslider1.setText("Off servo1")
            self.slider1.setEnabled(True)
            self.servo1 = Servo(self.servo1_pin)
        else:
            self.bslider1.setText("On servo1")
            self.slider1.setEnabled(False)
            self.slider1.setValue(0)
            self.servo1.stopped()
            self.servo1 = None
            print()

    def sliderservo2Act(self):
        print("Slider2servo")
        if (self.servo2 == None):
            self.bslider2.setText("Off servo1")
            self.slider2.setEnabled(True)
            self.servo2 = Servo(self.servo2_pin)
        else:
            self.bslider2.setText("On servo2")
            self.slider2.setEnabled(False)
            self.slider2.setValue(0)
            self.servo2.stopped()
            self.servo2 = None
            print()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())