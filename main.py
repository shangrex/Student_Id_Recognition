from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from interface import Ui_MainWindow
import cv2
import numpy as np
import math
import os
import sys

from interface import Ui_MainWindow

from run import predict_img
from ocr import text_reg

class UI_Interface(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(UI_Interface, self).__init__(parent)
        self.setupUi(self)

        self.predictButton.clicked.connect(self.predict)

    def predict(self):
        url = self.textEdit.toPlainText()

        ret = predict_img(url)
        text_reg(url, ret['rois'], ret['class_ids'])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UI_Interface()
    window.show()
    sys.exit(app.exec_())