# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/niklas/repositories/buttongame/buttongame/buttongameview.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ButtonGameView(object):
    def setupUi(self, ButtonGameView):
        ButtonGameView.setObjectName("ButtonGameView")
        ButtonGameView.resize(642, 441)
        ButtonGameView.setMinimumSize(QtCore.QSize(0, 0))
        self.centralWidget = QtWidgets.QWidget(ButtonGameView)
        self.centralWidget.setObjectName("centralWidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 50, 171, 271))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.labelFormLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.labelFormLayout.setContentsMargins(10, 10, 10, 10)
        self.labelFormLayout.setHorizontalSpacing(30)
        self.labelFormLayout.setVerticalSpacing(32)
        self.labelFormLayout.setObjectName("labelFormLayout")
        self.offen = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        self.offen.setFont(font)
        self.offen.setObjectName("offen")
        self.labelFormLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.offen)
        self.offenC = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.offenC.setFont(font)
        self.offenC.setObjectName("offenC")
        self.labelFormLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.offenC)
        self.korrekt = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        self.korrekt.setFont(font)
        self.korrekt.setObjectName("korrekt")
        self.labelFormLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.korrekt)
        self.korrektC = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.korrektC.setFont(font)
        self.korrektC.setObjectName("korrektC")
        self.labelFormLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.korrektC)
        self.falsch = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        self.falsch.setFont(font)
        self.falsch.setObjectName("falsch")
        self.labelFormLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.falsch)
        self.falschC = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.falschC.setFont(font)
        self.falschC.setObjectName("falschC")
        self.labelFormLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.falschC)
        self.gesamt = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        self.gesamt.setFont(font)
        self.gesamt.setObjectName("gesamt")
        self.labelFormLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.gesamt)
        self.gesamtC = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.gesamtC.setFont(font)
        self.gesamtC.setObjectName("gesamtC")
        self.labelFormLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.gesamtC)
        self.spiele = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        self.spiele.setFont(font)
        self.spiele.setObjectName("spiele")
        self.labelFormLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.spiele)
        self.spieleC = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.spieleC.setFont(font)
        self.spieleC.setObjectName("spieleC")
        self.labelFormLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spieleC)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(190, 50, 441, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.buttonGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.buttonGridLayout.setContentsMargins(11, 11, 11, 11)
        self.buttonGridLayout.setSpacing(6)
        self.buttonGridLayout.setObjectName("buttonGridLayout")
        self.btn1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn1.setMinimumSize(QtCore.QSize(75, 75))
        self.btn1.setMaximumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.btn1.setFont(font)
        self.btn1.setObjectName("btn1")
        self.buttonGridLayout.addWidget(self.btn1, 0, 0, 1, 1)
        self.btn4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn4.setMinimumSize(QtCore.QSize(75, 75))
        self.btn4.setMaximumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.btn4.setFont(font)
        self.btn4.setObjectName("btn4")
        self.buttonGridLayout.addWidget(self.btn4, 0, 3, 1, 1)
        self.btn3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn3.setMinimumSize(QtCore.QSize(75, 75))
        self.btn3.setMaximumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.btn3.setFont(font)
        self.btn3.setObjectName("btn3")
        self.buttonGridLayout.addWidget(self.btn3, 0, 2, 1, 1)
        self.btn2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn2.setMinimumSize(QtCore.QSize(75, 75))
        self.btn2.setMaximumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.btn2.setFont(font)
        self.btn2.setObjectName("btn2")
        self.buttonGridLayout.addWidget(self.btn2, 0, 1, 1, 1)
        self.btn6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn6.setMinimumSize(QtCore.QSize(75, 75))
        self.btn6.setMaximumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.btn6.setFont(font)
        self.btn6.setObjectName("btn6")
        self.buttonGridLayout.addWidget(self.btn6, 1, 0, 1, 1)
        self.btn11 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn11.setMinimumSize(QtCore.QSize(75, 75))
        self.btn11.setMaximumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.btn11.setFont(font)
        self.btn11.setObjectName("btn11")
        self.buttonGridLayout.addWidget(self.btn11, 2, 0, 1, 1)
        self.btn5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn5.setMinimumSize(QtCore.QSize(75, 75))
        self.btn5.setMaximumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.btn5.setFont(font)
        self.btn5.setObjectName("btn5")
        self.buttonGridLayout.addWidget(self.btn5, 0, 4, 1, 1)
        self.btn7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn7.setMinimumSize(QtCore.QSize(75, 75))
        self.btn7.setMaximumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.btn7.setFont(font)
        self.btn7.setObjectName("btn7")
        self.buttonGridLayout.addWidget(self.btn7, 1, 1, 1, 1)
        self.btn8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn8.setMinimumSize(QtCore.QSize(75, 75))
        self.btn8.setMaximumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.btn8.setFont(font)
        self.btn8.setObjectName("btn8")
        self.buttonGridLayout.addWidget(self.btn8, 1, 2, 1, 1)
        self.btn9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn9.setMinimumSize(QtCore.QSize(75, 75))
        self.btn9.setMaximumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.btn9.setFont(font)
        self.btn9.setObjectName("btn9")
        self.buttonGridLayout.addWidget(self.btn9, 1, 3, 1, 1)
        self.btn10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn10.setMinimumSize(QtCore.QSize(75, 75))
        self.btn10.setMaximumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.btn10.setFont(font)
        self.btn10.setObjectName("btn10")
        self.buttonGridLayout.addWidget(self.btn10, 1, 4, 1, 1)
        self.btn12 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn12.setMinimumSize(QtCore.QSize(75, 75))
        self.btn12.setMaximumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.btn12.setFont(font)
        self.btn12.setObjectName("btn12")
        self.buttonGridLayout.addWidget(self.btn12, 2, 1, 1, 1)
        self.btn13 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn13.setMinimumSize(QtCore.QSize(75, 75))
        self.btn13.setMaximumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.btn13.setFont(font)
        self.btn13.setObjectName("btn13")
        self.buttonGridLayout.addWidget(self.btn13, 2, 2, 1, 1)
        self.btn14 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn14.setMinimumSize(QtCore.QSize(75, 75))
        self.btn14.setMaximumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.btn14.setFont(font)
        self.btn14.setObjectName("btn14")
        self.buttonGridLayout.addWidget(self.btn14, 2, 3, 1, 1)
        self.btn15 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn15.setMinimumSize(QtCore.QSize(75, 75))
        self.btn15.setMaximumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.btn15.setFont(font)
        self.btn15.setObjectName("btn15")
        self.buttonGridLayout.addWidget(self.btn15, 2, 4, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 330, 621, 77))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.gmaeControlHorizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.gmaeControlHorizontalLayout.setContentsMargins(50, 11, 50, 11)
        self.gmaeControlHorizontalLayout.setSpacing(60)
        self.gmaeControlHorizontalLayout.setObjectName("gmaeControlHorizontalLayout")
        self.newGame = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.newGame.setMinimumSize(QtCore.QSize(0, 60))
        self.newGame.setObjectName("newGame")
        self.gmaeControlHorizontalLayout.addWidget(self.newGame)
        self.exit = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.exit.setMinimumSize(QtCore.QSize(0, 60))
        self.exit.setObjectName("exit")
        self.gmaeControlHorizontalLayout.addWidget(self.exit)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 611, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        ButtonGameView.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(ButtonGameView)
        self.mainToolBar.setObjectName("mainToolBar")
        ButtonGameView.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(ButtonGameView)
        self.statusBar.setObjectName("statusBar")
        ButtonGameView.setStatusBar(self.statusBar)

        self.retranslateUi(ButtonGameView)
        self.exit.clicked.connect(ButtonGameView.close)
        self.newGame.clicked.connect(ButtonGameView.startGame)
        self.btn1.clicked.connect(ButtonGameView.btnClicked)
        self.btn2.clicked.connect(ButtonGameView.btnClicked)
        self.btn3.clicked.connect(ButtonGameView.btnClicked)
        self.btn4.clicked.connect(ButtonGameView.btnClicked)
        self.btn5.clicked.connect(ButtonGameView.btnClicked)
        self.btn6.clicked.connect(ButtonGameView.btnClicked)
        self.btn7.clicked.connect(ButtonGameView.btnClicked)
        self.btn8.clicked.connect(ButtonGameView.btnClicked)
        self.btn9.clicked.connect(ButtonGameView.btnClicked)
        self.btn10.clicked.connect(ButtonGameView.btnClicked)
        self.btn11.clicked.connect(ButtonGameView.btnClicked)
        self.btn12.clicked.connect(ButtonGameView.btnClicked)
        self.btn13.clicked.connect(ButtonGameView.btnClicked)
        self.btn14.clicked.connect(ButtonGameView.btnClicked)
        self.btn15.clicked.connect(ButtonGameView.btnClicked)
        QtCore.QMetaObject.connectSlotsByName(ButtonGameView)

    def retranslateUi(self, ButtonGameView):
        _translate = QtCore.QCoreApplication.translate
        ButtonGameView.setWindowTitle(_translate("ButtonGameView", "ButtonGameView"))
        self.offen.setText(_translate("ButtonGameView", "offen:"))
        self.offenC.setText(_translate("ButtonGameView", "0"))
        self.korrekt.setText(_translate("ButtonGameView", "korrekt:"))
        self.korrektC.setText(_translate("ButtonGameView", "0"))
        self.falsch.setText(_translate("ButtonGameView", "falsch:"))
        self.falschC.setText(_translate("ButtonGameView", "0"))
        self.gesamt.setText(_translate("ButtonGameView", "gesamt:"))
        self.gesamtC.setText(_translate("ButtonGameView", "0"))
        self.spiele.setText(_translate("ButtonGameView", "Spiele:"))
        self.spieleC.setText(_translate("ButtonGameView", "0"))
        self.btn1.setText(_translate("ButtonGameView", "00"))
        self.btn4.setText(_translate("ButtonGameView", "00"))
        self.btn3.setText(_translate("ButtonGameView", "00"))
        self.btn2.setText(_translate("ButtonGameView", "00"))
        self.btn6.setText(_translate("ButtonGameView", "00"))
        self.btn11.setText(_translate("ButtonGameView", "00"))
        self.btn5.setText(_translate("ButtonGameView", "00"))
        self.btn7.setText(_translate("ButtonGameView", "00"))
        self.btn8.setText(_translate("ButtonGameView", "00"))
        self.btn9.setText(_translate("ButtonGameView", "00"))
        self.btn10.setText(_translate("ButtonGameView", "00"))
        self.btn12.setText(_translate("ButtonGameView", "00"))
        self.btn13.setText(_translate("ButtonGameView", "00"))
        self.btn14.setText(_translate("ButtonGameView", "00"))
        self.btn15.setText(_translate("ButtonGameView", "00"))
        self.newGame.setText(_translate("ButtonGameView", "Neues Spiel"))
        self.exit.setText(_translate("ButtonGameView", "Beenden"))
        self.label.setText(_translate("ButtonGameView", "Drücke die Buttons in der richtigen Reihenfolge!"))

