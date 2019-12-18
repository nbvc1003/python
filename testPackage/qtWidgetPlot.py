
import sys
import numpy as np
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from testPackage.qtWidgetPlotUI import Ui_Form

class Main(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

        self.setLayout(self.layout)
        # self.setGeometry(200, 200, 800, 600)

    def initUI(self):
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)

        # cb = QComboBox()
        # cb.addItem('Graph1')
        # cb.addItem('Graph2')
        # cb.activated[str].connect(self.onComboBoxChanged)
        # layout.addWidget(cb)

        self.layout = layout

        # self.onComboBoxChanged(cb.currentText())

    def doGraph1(self):
        x = np.arange(0, 10, 0.5)
        y1 = np.sin(x)
        y2 = np.cos(x)

        self.fig.clear()

        ax = self.fig.add_subplot(111)
        ax.plot(x, y1, label="sin(x)")
        ax.plot(x, y2, label="cos(x)", linestyle="--")

        ax.set_xlabel("x")
        ax.set_xlabel("y")

        ax.set_title("sin & cos")
        ax.legend()

        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    window.doGraph1()
    app.exec_()