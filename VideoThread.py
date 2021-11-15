
import cv2
import numpy as np
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
from numpy.core.arrayprint import printoptions
import time
#source: https://gist.github.com/docPhil99/ca4da12c9d6f29b9cea137b617c7b8b1
class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self, port):
        super().__init__()
        self._run_flag = True
        self.port = port

    def run(self):
        # capture from web cam
        cap = cv2.VideoCapture(self.port)
        while self._run_flag:
            ret, cv_img = cap.read()
            #cv_img = cv2.resize(cv_img, (320,240),interpolation=cv2.INTER_AREA)
            if ret:
                self.change_pixmap_signal.emit(cv_img)
            time.sleep(0.5)
        # shut down capture system
        cap.release()

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()
