from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import QTimer
from bs4 import BeautifulSoup as bs
import urllib.request as req, sys, time
from stockAnal.stock_analUI import Ui_MainWindow

# pyuic5 -x QtUIfilename.ui -o Pyfilename