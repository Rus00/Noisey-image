import os, sys

#sys.path.append('/home/rus/Desktop/UTK/cs493/semantic-segmentation-pytorch')
#from predict_img import *
from noise_video_gen import *
from noise_image import *

from PyQt5 import QtCore, QtWidgets, QtGui
from window import Ui_MainWindow


class mainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)

        self.ui.pushButton_browse_file.clicked.connect(lambda : self.file_browse(self.ui.lineEdit_filename))
        self.ui.pushButton_browse_file_2.clicked.connect(lambda: self.file_browse(self.ui.lineEdit_filename_2))
        self.ui.pushButton.clicked.connect(self.noise_gen)
        self.ui.pushButton_2.clicked.connect(self.start_model)
        
        self.ui.pb_noise_gen.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.pb_sementic_seg.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.pb_back.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        self.ui.pb_back_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))

        self.ui.checkBox.stateChanged.connect(lambda: self.ui.lineEdit_filename_2.setText(self.ui.lineEdit.text() + ".jpg"))

    def file_browse(self, lineEdit):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, "Select image", filter="Image files (*.jpg *.png)")
       
        lineEdit.setText(fileName[0])
        print(fileName[0])
        
        if(lineEdit == self.ui.lineEdit_filename):
            self.ui.preview.setPixmap(QtGui.QPixmap(lineEdit.text()))

    def noise_gen(self):
        
        img = self.ui.lineEdit_filename.text()
        noise_level = self.ui.doubleSpinBox.value()
        out = self.ui.lineEdit.text() + ".jpg"
        add_noise_img(img, noise_level, out)
        self.ui.preview.setPixmap(QtGui.QPixmap(out))

    def start_model(self):
        start_from_gui(self.ui.lineEdit_filename_2.text())

if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    window = mainWindow()
    window.show()

    app.exec_()