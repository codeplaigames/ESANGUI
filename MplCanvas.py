import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
#source: https://www.pythonguis.com/tutorials/plotting-matplotlib/
class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        
        self.ejex = []
        self.ax = []
        self.ay = []
        self.az = []
        self.gx = []
        self.gy = []
        self.gz = []
        super(MplCanvas, self).__init__(fig)

    def drawio(self, dx):
        n = len(self.ejex)
        if(n == 20):
            #self.ejex.pop(0)
            self.ax.pop(0)
            self.ay.pop(0)
            self.az.pop(0)
            self.gx.pop(0)
            self.gy.pop(0)
            self.gz.pop(0)
        else:
            self.ejex.append(n)
        
        self.ax.append(dx[0])
        self.ay.append(dx[1])
        self.az.append(dx[2])
        self.gx.append(dx[3])
        self.gy.append(dx[4])
        self.gz.append(dx[5])

        #clear canvas
        self.axes.cla()# clear the canvas
        self.axes.plot(self.ejex, self.ax,'b')
        self.axes.plot(self.ejex, self.ay,'g')
        self.axes.plot(self.ejex, self.az,'r')
        self.axes.plot(self.ejex, self.gx,'c')
        self.axes.plot(self.ejex, self.gy,'m')
        self.axes.plot(self.ejex, self.gz,'k')
        self.axes.legend(['Ax','Ay','Az','Gx','Gy','Gz'])

        self.draw()

        

