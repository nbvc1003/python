from datetime import date
from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
from numpy import polyval
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from testPackage.testMainUI import Ui_MainWindow
# from scipy import stats
import random, sys, time

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.iniUI()
        self.inputData()

    def iniUI(self):
        self.m = PlotCanvas(self, width=5, height=4)
        self.m.move(100, 200)

        self.show()

    # 콜솔 출력부프린트
    def ConsolePrint(slope=0, intersecept=0, r_value=0, p_value=0):
        print('기울기 :', slope)
        print('절편 :', intersecept)
        print('상관계수 :', r_value)
        print('유의수준 :', p_value)

    # 그래프 출력부
    def MPlot(plt, tsd , csd, slope, intersecept):
        # print(tsd , csd, slope, intersecept)
        ry = polyval([slope, intersecept], tsd)
        plt.plot(tsd, csd, 'k.')
        plt.plot(tsd, ry, 'r')
        # plt.title('{}/{}'.format(targetStockCode, compStockCode))
        # plt.xlabel(targetStockCode)
        # plt.ylabel(compStockCode)
        # plt.legend(['price', 'polyval'])
        # plt.show()

    def inputData(self):
        try:
            d = date.today()
            start = date(2019, 1, 1)
            end = date(d.year, d.month, d.day)
            # targetStock_df = data.DataReader(targetStockCode, "yahoo", start, end)  # start ~ end 까지
            # compStock_df = data.DataReader(compStockCode, "yahoo", start, end)  # start ~ end 까지
            targetStock_df = data.DataReader("AMD", "yahoo", start, end)  # start ~ end 까지
            compStock_df = data.DataReader("AAPL", "yahoo", start, end)  # start ~ end 까지
        except RemoteDataError as ede:
            # print(type(ede))
            print('애러발생 {}'.format(ede))
            pass
        except Exception as err:
            print(type(err))
            pass
        tsd = []
        csd = []
        tsd = list(targetStock_df['Close'])
        csd = list(compStock_df['Close'])
        # slope, intersecept, r_value, p_value, stderr = stats.linregress(tsd, csd)
        # ConsolePrint(slope, intersecept, r_value, p_value)
        # MPlot(plt, tsd, csd, slope, intersecept)
        # print(tsd, type(tsd))
        # ry = polyval([slope, intersecept], tsd)
        # print(targetStock_df['Close'])
        self.m.plot(tsd, csd, markup='k.')
        # self.m.plot(tsd, ry, markup='r')


class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        # self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.ax = self.figure.add_subplot(111)

    def plot(self, *data, markup = None, title = 'NoTitle', xLabel = None, yLabel = None):
        if len(data) == 0:
            data = [random.random() for i in range(25)]
        if markup is None:
            markup = 'k.'
        # ax = self.figure.add_subplot(111)
        self.ax.plot(data[0], data[1], markup)
        self.ax.set_title(title)
        self.draw()

    def plotClear(self):
        self.ax.plot()
        self.ax.set_title("title")
        self.draw()


app = QApplication([])
ex = Main()

sys.exit(app.exec_())
