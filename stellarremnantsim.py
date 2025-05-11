#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Imports
import numpy as np
import matplotlib.pyplot as plt
import scipy as scp
from tabulate import tabulate
from matplotlib import image as img
import time
import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
import sys

#---------------------------------------------
# Main code

class Window(QMainWindow):
    singleton: 'Window' = None
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stellar Remnant Simulation") # setting title
        self.setGeometry(100, 100, 600, 600)  # setting geometry
        self.UiComponents() # calling method
        self.show() # showing all the widgets
        self.setStyleSheet("background-color: black") # setting the background color of the screen

    def UiComponents(self):

        self.loading = QPushButton("PUSH TO START", self) # creating a button to begin the game
        self.loading.setGeometry(0, 0, 600, 600) # setting geometry of button
        self.loading.setStyleSheet("color: white; background-color: black") # setting text color and background color
        self.loading.clicked.connect(self.showstars) # adding action to the button

        self.tiny = QPushButton("Tiny star", self) # creating a button to select a tiny star
        self.tiny.setGeometry(80, 250, 80, 80)
        self.tiny.setStyleSheet("color: black; border-radius : 40; border : 2px solid black; background-color: red")
        self.tiny.clicked.connect(self.browndwarf)
        self.tiny.hide()
        
        self.sunlike = QPushButton("Sun-like star", self) # creating a button to select a Sun-like star
        self.sunlike.setGeometry(180, 230, 120, 120)
        self.sunlike.setStyleSheet("color: black; border-radius : 60; border : 2px solid black; background-color: yellow")
        self.sunlike.clicked.connect(self.sunstar)
        self.sunlike.hide()
 
        self.large = QPushButton("Large star", self) # creating a button to select a large star
        self.large.setGeometry(320, 190, 200, 200)
        self.large.setStyleSheet("color: black; border-radius : 100; border : 2px solid black; background-color: blue")
        self.large.clicked.connect(self.largestar)
        self.large.hide()

        self.yes = QPushButton("Yes", self) # creating a button to select a large star
        self.yes.setGeometry(210, 450, 80, 50)
        self.yes.setStyleSheet("color: white; border-radius : 40; border : 2px solid white; background-color: black")
        self.yes.clicked.connect(self.yesclick)
        self.yes.hide()

        self.no = QPushButton("No", self)
        self.no.setGeometry(330, 450, 80, 50)
        self.no.setStyleSheet("color: white; border-radius : 40; border : 2px solid white; background-color: black")
        self.no.clicked.connect(self.noclick)
        self.no.hide()

        self.yes2 = QPushButton("Yes", self)
        self.yes2.setGeometry(210, 450, 80, 50)
        self.yes2.setStyleSheet("color: white; border-radius : 40; border : 2px solid white; background-color: black")
        self.yes2.clicked.connect(self.yesclick2)
        self.yes2.hide()

        self.no2 = QPushButton("No", self)
        self.no2.setGeometry(330, 450, 80, 50)
        self.no2.setStyleSheet("color: white; border-radius : 40; border : 2px solid white; background-color: black")
        self.no2.clicked.connect(self.noclick2)
        self.no2.hide()

        self.big = QPushButton("Big", self)
        self.big.setGeometry(210, 450, 80, 50)
        self.big.setStyleSheet("color: white; border-radius : 40; border : 2px solid white; background-color: black")
        self.big.clicked.connect(self.bigclick)
        self.big.hide()

        self.rbig = QPushButton("REALLY Big", self)
        self.rbig.setGeometry(330, 450, 80, 50)
        self.rbig.setStyleSheet("color: white; border-radius : 40; border : 2px solid white; background-color: black")
        self.rbig.clicked.connect(self.bh)
        self.rbig.hide()

        self.small = QPushButton("Small", self)
        self.small.setGeometry(210, 450, 80, 50)
        self.small.setStyleSheet("color: white; border-radius : 40; border : 2px solid white; background-color: black")
        self.small.clicked.connect(self.ns)
        self.small.hide()

        self.big2 = QPushButton("Big", self)
        self.big2.setGeometry(330, 450, 80, 50)
        self.big2.setStyleSheet("color: white; border-radius : 40; border : 2px solid white; background-color: black")
        self.big2.clicked.connect(self.bh)
        self.big2.hide()

        self.reset = QPushButton("Reset Game", self)
        self.reset.setGeometry(250, 540, 80, 50)
        self.reset.setStyleSheet("color: white; border-radius : 40; border : 2px solid white; background-color: black")
        self.reset.clicked.connect(self.resetgame)
        self.reset.hide()

        self.accrete = QPushButton("Press to accrete!", self)
        self.accrete.setGeometry(250, 500, 125, 50)
        self.accrete.setStyleSheet("color: white; border-radius : 40; border : 2px solid white; background-color: black")
        self.accrete.clicked.connect(self.accretemass)
        self.accrete.hide()

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap())

        self.text = QLabel(self)
        self.text.setStyleSheet("color: white")
        self.text.move(200, 50)
        self.text.hide()

        self.text2 = QLabel(self)
        self.text2.setStyleSheet("color: white")
        self.text2.move(200, 425)
        self.text2.hide()

        self.movie = QMovie("accretion.gif")

        self.counter_value = 0
        self.counter_label = QLabel(self)
        self.counter_label.setAlignment(Qt.AlignCenter)
        self.counter_label.setStyleSheet("color: white")
        self.counter_label.setGeometry(275, 275, 50, 50)
        self.counter_label.hide()

        self.resettimer = QTimer()
        self.resettimer.setSingleShot(True)
        self.resettimer.timeout.connect(self.resetgame)
        self.resettimer.start(90000)

    def showstars(self):
        self.tiny.show()
        self.sunlike.show()
        self.large.show()
        self.loading.hide()

    def browndwarf(self):
        self.tiny.hide()
        self.sunlike.hide()
        self.large.hide()
        self.pixmap = QPixmap('browndwarf.jpg')
        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)
        self.label.setFixedHeight(600)
        self.label.setFixedWidth(600)
        self.text.setText("You've created a Brown Dwarf!")
        self.text.adjustSize() 
        self.text.show()
        self.reset.show()
        self.reset.raise_()
        
    def sunstar(self):
        self.tiny.hide()
        self.sunlike.hide()
        self.large.hide()
        self.pixmap = QPixmap('redgiant.jpg')
        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)
        self.label.setFixedHeight(600)
        self.label.setFixedWidth(600)
        self.text.setText("Your star has turned into a Red Giant!")
        self.text.adjustSize() 
        self.text.show()
        self.text2.setText("Does your star have a friend nearby?")
        self.text2.adjustSize() 
        self.text2.show()
        self.yes.show()
        self.yes.raise_()
        self.no.show()
        self.no.raise_()

    def largestar(self):
        self.tiny.hide()
        self.sunlike.hide()
        self.large.hide()
        self.pixmap = QPixmap('redsupergiant')
        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)
        self.label.setFixedHeight(600)
        self.label.setFixedWidth(600)
        self.text.setText("Your star has turned into a Red Supergiant!")
        self.text.adjustSize() 
        self.text.show()
        self.text2.setText("Is your star big or REALLY big?")
        self.text2.adjustSize() 
        self.text2.show()
        self.text2.move(215, 425)
        self.big.show()
        self.big.raise_()
        self.rbig.show()
        self.rbig.raise_()

    def wd(self):
        self.pixmap = QPixmap('whitedwarf.jpg')
        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)
        self.label.setFixedHeight(600)
        self.label.setFixedWidth(600)
        self.text.setText("Your star has turned into a White Dwarf!")
        self.text.adjustSize() 
        self.text.show()
        self.reset.show()
        self.reset.raise_()

    def yesclick(self):
        self.text.hide()
        self.text2.hide()
        self.yes.hide()
        self.no.hide()
        self.pixmap = QPixmap('binarywd')
        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)
        self.label.setFixedHeight(600)
        self.label.setFixedWidth(600)
        self.text.setText("Your star is in a binary system!")
        self.text.adjustSize() 
        self.text.show()
        QTimer.singleShot(3000, self.accretion)

    def noclick(self):
        self.text.hide()
        self.text2.hide()
        self.yes.hide()
        self.no.hide() 
        self.pixmap = QPixmap('planetarynebula.jpg')
        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)
        self.label.setFixedHeight(600)
        self.label.setFixedWidth(600)
        self.text.setText("Your star has exploded into a Planetary Nebula!")
        self.text.adjustSize() 
        self.text.show()
        QTimer.singleShot(3000, self.wd)

    def yesclick2(self):
        self.text.hide()
        self.text2.hide()
        self.yes2.hide()
        self.no2.hide()
        self.pixmap = QPixmap('supernova.jpg')
        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)
        self.label.setFixedHeight(600)
        self.label.setFixedWidth(600)
        self.text.setText("Your star has exploded into a Type Ia Supernova!")
        self.text.adjustSize() 
        self.text.show()
        self.reset.show()
        self.reset.raise_()

    def noclick2(self):
        self.text.hide()
        self.text2.hide()
        self.yes2.hide()
        self.no2.hide() 
        self.pixmap = QPixmap('nova')
        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)
        self.label.setFixedHeight(600)
        self.label.setFixedWidth(600)
        self.text.setText("Your star has exploded into a Nova!")
        self.text.adjustSize() 
        self.text.show()
        QTimer.singleShot(3000, self.wd)

    def accretion(self):
        self.text2.setText("Uh oh! The companion star is taking a lot of your star's mass! Should we stop it?")
        self.text2.move(50, 425)
        self.text2.adjustSize() 
        self.text2.show()
        self.yes2.show()
        self.yes2.raise_()
        self.no2.show()
        self.no2.raise_()

    def bh(self):
        self.resettimer.stop()
        self.rbig.hide()
        self.big.hide()
        self.text.hide()
        self.text2.hide()
        self.pixmap = QPixmap('blackhole')
        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)
        self.label.setFixedHeight(600)
        self.label.setFixedWidth(600)
        self.text.setText("You've created a black hole!")
        self.text.adjustSize() 
        self.text.show()
        self.text2.setText("BONUS ROUND - Accretion Game - Initiated!")
        self.text2.move(165, 425)
        self.text2.adjustSize() 
        self.text2.show()
        self.big2.hide()
        self.small.hide()
        self.reset.show()
        self.reset.raise_()
        QTimer.singleShot(2000, self.bonusround)

    def bonusround(self):
        self.text.setText("Press the button below to accrete as much mass as you can in 30 seconds!")
        self.text.move(50, 50)
        self.text.adjustSize() 
        self.text.raise_()
        self.text.show()
        self.text2.hide()
        self.reset.hide()
        self.label.setMovie(self.movie)
        self.movie.start()
        self.label.setScaledContents(True)
        self.label.setFixedHeight(600)
        self.label.setFixedWidth(600)
        self.label.setMovie(self.movie)
        self.accrete.show()
        self.accrete.raise_()
        QTimer.singleShot(30000, self.endscreen)
        
    def accretemass(self):
        self.counter_value += 1
        self.counter_label.setText(str(f"{self.counter_value}"))
        self.counter_label.show()

    def endscreen(self):
        self.accrete.hide()
        self.reset.show()
        self.text2.show()
        self.text2.adjustSize() 
        self.text.move(200,50)
        if self.counter_value < 80:
            self.text.setText(f"You've accreted {self.counter_value} solar masses!")
            self.text2.setText("You've created a solar mass black hole!")
            self.text2.adjustSize() 
        if self.counter_value in range (100, 130):
            self.text.setText(f"You've accreted {self.counter_value*10} solar masses!")
            self.text2.setText("You've created an intermediate mass black hole!")
            self.text2.adjustSize() 
        if self.counter_value > 130:  
            self.text.setText(f"You've accreted {self.counter_value*100} solar masses!")
            self.text2.setText("You've created a supermassive black hole!")
            self.text2.adjustSize() 
        QTimer.singleShot(20000, self.resetgame)
        
    def bigclick(self):
        self.rbig.hide()
        self.big.hide()
        self.text.hide()
        self.text2.hide()
        self.pixmap = QPixmap('supernova.jpg')
        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)
        self.label.setFixedHeight(600)
        self.label.setFixedWidth(600)
        self.text.setText("Your star has exploded into a Type II Supernova!")
        self.text.adjustSize() 
        self.text.show()
        self.text2.setText("Is your left over stellar core small or big?")
        self.text2.adjustSize() 
        self.text2.show()
        self.text2.move(215, 425)
        self.big2.show()
        self.big2.raise_()
        self.small.show()
        self.small.raise_()

    def ns(self):
        self.big2.hide()
        self.small.hide()
        self.text.hide()
        self.text2.hide()
        self.pixmap = QPixmap('neutronstar')
        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)
        self.label.setFixedHeight(600)
        self.label.setFixedWidth(600)
        self.text.setText("You've created a neutron star!")
        self.text.adjustSize() 
        self.text.show()
        self.reset.show()
        self.reset.raise_()

    def resetgame(self):
        Window.singleton = Window()
        
          
   
# create pyqt5 app
App = QApplication(sys.argv)
 
# create the instance of our Window
window = Window()
 
# start the app
sys.exit(App.exec())


# In[ ]:


# Image references
# Brown dwarf: https://earthsky.org/space/tiny-brown-dwarf-ic-348-star-cluster-webb/
# Red giant: https://www.forbes.com/sites/jamiecartereurope/2019/07/25/a-hiccup-and-the-end-of-history-what-the-pulse-of-a-red-giant-star-tells-us-about-armageddon/
# White dwarf: https://www.space.com/23756-white-dwarf-stars.html
# Planetary nebula: https://www.skyatnightmagazine.com/space-science/planetary-nebula
# Binary white dwarf: https://www.astronomy.com/science/rare-pulsating-white-dwarf-spotted-in-a-binary-star-system/
# Supernova: https://www.sci.news/astronomy/two-supernovae-act-exploding-03719.html
# Nova: https://www.earth.com/news/t-coronae-borealis-nova-explosion-nearby-star-light-up-earths-skies/
# Red supergiant: https://www.robinage.com/final-explosion-of-red-supergiant-star/
# Neutron star: https://www.physik.tu-darmstadt.de/aktuelles_physik/news_details_96640.en.jsp
# Black hole: https://mashable.com/article/primordial-black-holes-evidence-everyday-objects
# Accretion disk: https://svs.gsfc.nasa.gov/13326

