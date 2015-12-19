#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from random import shuffle

from view import Ui_ButtonGameView

class Controller(QMainWindow):
    """
    Controller fuer das Button Spiel
    """

    next = 1
    open = 15
    right = 0
    wrong = 0
    games = -1


    def __init__(self, parent=None):
        """
        Initialisiert die View und startet das erste Spiel
        """
        super().__init__(parent)
        self.view = Ui_ButtonGameView()
        self.view.setupUi(self)
        self.startGame()

    def startGame(self):
        """
        Setzt den Text der Buttons in zufaelliger Reihenfolge und aktiviert
        sie alle. Dannach werden die Zaehler wieder zurueckgesetzt. Wird auch
        durch Klick auf den Button "Neues Spiel" ausgefuehrt.
        """
        numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        shuffle(numbers)
        self.view.btn1.setText(str(numbers[0]))
        self.view.btn1.setEnabled(True)
        self.view.btn2.setText(str(numbers[1]))
        self.view.btn2.setEnabled(True)
        self.view.btn3.setText(str(numbers[2]))
        self.view.btn3.setEnabled(True)
        self.view.btn4.setText(str(numbers[3]))
        self.view.btn4.setEnabled(True)
        self.view.btn5.setText(str(numbers[4]))
        self.view.btn5.setEnabled(True)
        self.view.btn6.setText(str(numbers[5]))
        self.view.btn6.setEnabled(True)
        self.view.btn7.setText(str(numbers[6]))
        self.view.btn7.setEnabled(True)
        self.view.btn8.setText(str(numbers[7]))
        self.view.btn8.setEnabled(True)
        self.view.btn9.setText(str(numbers[8]))
        self.view.btn9.setEnabled(True)
        self.view.btn10.setText(str(numbers[9]))
        self.view.btn10.setEnabled(True)
        self.view.btn11.setText(str(numbers[10]))
        self.view.btn11.setEnabled(True)
        self.view.btn12.setText(str(numbers[11]))
        self.view.btn12.setEnabled(True)
        self.view.btn13.setText(str(numbers[12]))
        self.view.btn13.setEnabled(True)
        self.view.btn14.setText(str(numbers[13]))
        self.view.btn14.setEnabled(True)
        self.view.btn15.setText(str(numbers[14]))
        self.view.btn15.setEnabled(True)
        self.games+=1
        self.view.spieleC.setText(str(self.games))
        self.next=1
        self.open=15
        self.view.offenC.setText(str(self.open))

    def btnClicked(self):
        """
        Wird aufgerufen sobald ein Button mit einer Zahl darauf gedrueckt wird.
        Falls die Reihenfolge richtig war, wird der Button deaktiviert und die
        Zaehler werden entsprechend gesetzt. Wenn alle Buttons richtig gedrueckt
        wurden, wird das Spiel neu gestartet.
        """
        eventsrc = getattr(self.view, self.sender().objectName())
        if eventsrc.text() == str(self.next):
            self.right+=1
            self.next+=1
            self.open-=1

            eventsrc.setEnabled(False)
            self.view.korrektC.setText(str(self.right))
            self.view.offenC.setText(str(self.open))
        else:
            self.wrong+=1
            self.view.falschC.setText(str(self.wrong))

        self.view.gesamtC.setText(str(self.right+self.wrong))

        if self.next == 16:
            self.startGame()
