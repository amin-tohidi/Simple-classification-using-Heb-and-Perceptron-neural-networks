from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys 
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import numpy as np 
from numpy import random

from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.layers import Dense,Dropout,Flatten

from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon



class Ui_AminTohidi(object):
    def setupUi(self, AminTohidi):
        AminTohidi.setObjectName("AminTohidi")
        AminTohidi.resize(900, 500)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        AminTohidi.setFont(font)
        AminTohidi.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(AminTohidi)
        self.centralwidget.setObjectName("centralwidget")
        self.showdata = QtWidgets.QPushButton(self.centralwidget)
        self.showdata.setGeometry(QtCore.QRect(60, 200, 201, 31))
        self.showdata.setObjectName("showdata")
        self.meyangin1 = QtWidgets.QLineEdit(self.centralwidget)
        self.meyangin1.setGeometry(QtCore.QRect(9, 120, 71, 20))
        self.meyangin1.setObjectName("meyangin1")
        self.enheraf1 = QtWidgets.QLineEdit(self.centralwidget)
        self.enheraf1.setGeometry(QtCore.QRect(9, 90, 71, 20))
        self.enheraf1.setObjectName("enheraf1")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(160, 60, 20, 131))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 60, 81, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 60, 81, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 90, 81, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 120, 51, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 150, 41, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(260, 150, 41, 20))
        self.label_6.setObjectName("label_6")
        self.enheraf2 = QtWidgets.QLineEdit(self.centralwidget)
        self.enheraf2.setGeometry(QtCore.QRect(180, 90, 71, 20))
        self.enheraf2.setObjectName("enheraf2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(260, 120, 51, 20))
        self.label_7.setObjectName("label_7")
        self.meyangin2 = QtWidgets.QLineEdit(self.centralwidget)
        self.meyangin2.setGeometry(QtCore.QRect(180, 120, 71, 20))
        self.meyangin2.setObjectName("meyangin2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(250, 90, 81, 21))
        self.label_8.setObjectName("label_8")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 180, 291, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.perseptron = QtWidgets.QPushButton(self.centralwidget)
        self.perseptron.setGeometry(QtCore.QRect(170, 350, 131, 31))
        self.perseptron.setObjectName("perseptron")
        self.tedad1 = QtWidgets.QSpinBox(self.centralwidget)
        self.tedad1.setGeometry(QtCore.QRect(30, 150, 51, 22))
        self.tedad1.setMaximum(1000000000)
        self.tedad1.setMinimum(1)
        self.tedad1.setObjectName("tedad1")
        self.tedad2 = QtWidgets.QSpinBox(self.centralwidget)
        self.tedad2.setGeometry(QtCore.QRect(200, 150, 51, 22))
        self.tedad2.setMaximum(1000000000)
        self.tedad2.setMinimum(1)
        self.tedad2.setDisplayIntegerBase(10)
        self.tedad2.setObjectName("tedad2")
        self.heb = QtWidgets.QPushButton(self.centralwidget)
        self.heb.setGeometry(QtCore.QRect(20, 350, 131, 31))
        self.heb.setObjectName("heb")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(620, 430, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.exit.setFont(font)
        self.exit.setMouseTracking(False)
        self.exit.setObjectName("exit")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 20, 900, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(340, 50, 550, 371))
        self.textBrowser.setObjectName("textBrowser")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(20, 230, 291, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(140, 290, 171, 16))
        self.label_9.setObjectName("label_9")
        self.epocke = QtWidgets.QSpinBox(self.centralwidget)
        self.epocke.setGeometry(QtCore.QRect(80, 290, 51, 22))
        self.epocke.setMaximum(500000)
        self.epocke.setMinimum(1)
        self.epocke.setObjectName("epocke")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(110, 30, 91, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(80, 250, 131, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(480, 0, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(490, 30, 91, 20))
        font = QtGui.QFont()
        font.setItalic(False)
        font.setUnderline(False)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        AminTohidi.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AminTohidi)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 735, 21))
        self.menubar.setObjectName("menubar")
        AminTohidi.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AminTohidi)
        self.statusbar.setObjectName("statusbar")
        AminTohidi.setStatusBar(self.statusbar)
     
        
        self.retranslateUi(AminTohidi)
        self.showdata.clicked.connect(self.show_data)
        self.perseptron.clicked.connect(self.amin)
        self.exit.clicked.connect(AminTohidi.close)
        self.heb.clicked.connect(self.amin)
        QtCore.QMetaObject.connectSlotsByName(AminTohidi)
    
    def show_data(self):
        if self.enheraf1.text() =="":
            if self.meyangin1.text() =="":
                if self.enheraf2.text() =="": 
                    if self.meyangin2.text() =="":           
                        self.textBrowser.clear()
                        img_gen=ImageDataGenerator(rescale=1./255, validation_split=0.2)
                        train_set=img_gen.flow_from_directory('C:/Users/AMIN/Desktop/Dataset',
                                                              target_size=(28,28), batch_size=32,
                                                              class_mode='categorical', 
                                                              color_mode='grayscale', 
                                                              subset='training',  
                                                              seed=1)
                                          
                        valid_set=img_gen.flow_from_directory('C:/Users/AMIN/Desktop/Dataset',
                                              target_size=(28,28),
                                              batch_size=32,
                                              class_mode='categorical',
                                              color_mode='grayscale',
                                              subset='validation',
                                              seed=1)
                        
                                               
                                                
                        model = Sequential()
                        
                        model.add(Flatten())
                        
                        #input layer
                        model.add(Dense(512,activation='tanh'))
                        # Hiden layer 1
                        model.add(Dense(512, activation='tanh'))
                        # Hiden layer 2
                        model.add(Dense(512, activation='tanh'))
                        # output layer
                        model.add(Dense(4, activation='softmax'))
                        
                        
                        #Determining learning rate and error and optimizer functions 
                        model.compile(loss='categorical_crossentropy',
                                      optimizer=Adam(learning_rate=0.001, name='Adam'),
                                      metrics = ["accuracy"])
                        history = model.fit(x=train_set,validation_data=valid_set,
                                            epochs=2, verbose=1)
                        xx=max(history.history['accuracy'])
                        yy=min(history.history['loss'])
                        self.textBrowser.append('accuracy:    ' + (str(xx)))
                        self.textBrowser.append('loss:     ' +str(yy))
                      
                        
                      
                      # self.textBrowser.append(history )
                        model.save("dast_khat.h5")
                       
      
        else:

            self.textBrowser.append("لطفا مقادیر مشخص شده را وارد نمایید. ")
    
  
    
           
            
    def amin(self) :
        class Window(QMainWindow): 
        	def __init__(self): 
        		super().__init__() 
        		# setting title 
        		self.setWindowTitle("Paint with PyQt5") 
        		# setting geometry to main window 
        		self.setGeometry(100, 100, 800, 600) 
        		# creating image object 
        		self.image = QImage(self.size(), QImage.Format_RGB32) 
        		# making imae color to white 
        		self.image.fill(Qt.white) 
        		# variables 
        		# drawing flag 
        		self.drawing = False
        		# default brush size 
        		self.brushSize = 2
        		# default color 
        		self.brushColor = Qt.black 
        		# QPoint object to tract the point 
        		self.lastPoint = QPoint() 
        		# creating menu bar 
        		mainMenu = self.menuBar() 
        		# creating file menu for save and clear action 
        		fileMenu = mainMenu.addMenu("File") 
        		# creatng save action 
        		saveAction = QAction("Save", self) 
        		# adding short cut for save action 
        		saveAction.setShortcut("Ctrl + S") 
        		# adding save to the file menu 
        		fileMenu.addAction(saveAction) 
        		# adding action to the save 
        		saveAction.triggered.connect(self.save) 
        		# creating clear action 
        		clearAction = QAction("Clear", self) 
        		# adding short cut to the clear action 
        		clearAction.setShortcut("Ctrl + C") 
        		# adding clear to the file menu 
        		fileMenu.addAction(clearAction) 
        		# adding action to the clear 
        		clearAction.triggered.connect(self.clear) 
        		# creating action for selecting pixel of 4px 
        		pix_4 = QAction("4px", self) 
        		# adding method to this 
        		pix_4.triggered.connect(self.Pixel_4) 
        		black = QAction("Black", self) 
        		# adding methods to the black 
        		black.triggered.connect(self.blackColor) 
        	# method for checking mouse cicks 
        	def mousePressEvent(self, event): 
        		# if left mouse button is pressed 
        		if event.button() == Qt.LeftButton: 
        			# make drawing flag true 
        			self.drawing = True
        			# make last point to the point of cursor 
        			self.lastPoint = event.pos() 
        	# method for tracking mouse activity 
        	def mouseMoveEvent(self, event): 
        		# checking if left button is pressed and drawing flag is true 
        		if (event.buttons() & Qt.LeftButton) & self.drawing: 
        			# crating painter object 
        			painter = QPainter(self.image) 
        			# set the pen of the painter 
        			painter.setPen(QPen(self.brushColor, self.brushSize, 
        							Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)) 
        			# this will draw only one step 
        			painter.drawLine(self.lastPoint, event.pos()) 
        			# change the last point 
        			self.lastPoint = event.pos() 
        			# update 
        			self.update() 
        	# method for mouse left button release 
        	def mouseReleaseEvent(self, event): 
        		if event.button() == Qt.LeftButton: 
        			# make drawing flag false 
        			self.drawing = False
        	# paint event 
        	def paintEvent(self, event): 
        		# create a canvas 
        		canvasPainter = QPainter(self) 
        		# draw ectangle on the canvas 
        		canvasPainter.drawImage(self.rect(), self.image, self.image.rect()) 
        	# method for saving canvas 
        	def save(self): 
        		filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "", 
        						"PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ") 
        		if filePath == "": 
        			return
        		self.image.save(filePath) 
        	# method for clearing every thing on canvas 
        	def clear(self): 
        		# make the whole canvas white 
        		self.image.fill(Qt.white) 
        		# update 
        		self.update() 
        	# methods for changing pixel sizes 
        	def Pixel_4(self): 
        		self.brushSize = 4
        	# methods for changing brush color 
        	def blackColor(self): 
        		self.brushColor = Qt.black 
        # create pyqt5 app 
      
                
       
        
       
        
       
        
       
        
       
        

    def retranslateUi(self, AminTohidi):
        _translate = QtCore.QCoreApplication.translate
        AminTohidi.setWindowTitle(_translate("AminTohidi", "MainWindow"))
        self.showdata.setText(_translate("AminTohidi", "نمايش داده ها"))
        self.label.setText(_translate("AminTohidi", "دسته اول (A)"))
        self.label_2.setText(_translate("AminTohidi", "دسته دوم (B)"))
        self.label_3.setText(_translate("AminTohidi", "انحراف معيار ="))
        self.label_4.setText(_translate("AminTohidi", "ميانگين ="))
        self.label_5.setText(_translate("AminTohidi", "تعداد ="))
        self.label_6.setText(_translate("AminTohidi", "تعداد ="))
        self.label_7.setText(_translate("AminTohidi", "ميانگين ="))
        self.label_8.setText(_translate("AminTohidi", "انحراف معيار ="))
        self.perseptron.setText(_translate("AminTohidi", "شبکه عصبي پرسپترون"))
        self.heb.setText(_translate("AminTohidi", "شبکه عصبي هب"))
        self.exit.setText(_translate("AminTohidi", "خروج"))
        self.label_9.setText(_translate("AminTohidi", "لطفا تعداد تکرار را مشخص کنيد :"))
        self.label_10.setText(_translate("AminTohidi", "معرفي داده ها "))
        self.label_11.setText(_translate("AminTohidi", "انتخاب نوع شبکه عصبي"))
        self.label_12.setText(_translate("AminTohidi", "امين توحيدي فر 991419017 "))
        self.label_13.setText(_translate("AminTohidi","نمايش محاسبات"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AminTohidi = QtWidgets.QMainWindow()
    ui = Ui_AminTohidi()
    ui.setupUi(AminTohidi)
    AminTohidi.show()
    sys.exit(app.exec_())
