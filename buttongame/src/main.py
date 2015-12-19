#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

from controller import Controller

if __name__ == "__main__":
    """
    Startet die App und initialisiert den Controller
    """
    app = QApplication(sys.argv)
    c = Controller()
    c.show()
    sys.exit(app.exec_())
