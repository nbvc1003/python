from pandas_datareader import data
from datetime import date
import pandas as pd
import statsmodels.formula.api as sm
import matplotlib.pyplot as plt

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 차트에 한글 가능하도록
from matplotlib import font_manager, rc, rcParams
font_name = font_manager.FontProperties(
    fname="c:/windows/Fonts/malgun.ttf").get_name()
rc('font',family=font_name)
rcParams['axes.unicode_minus'] = False # 부호표시 (-,+) 사용할때
###
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 종목 코드 1
# 종목 코드 2
# 날짜1 ~ 날짜2
# 분석 시작
#

d = date.today()
start = date(2019,1,1)
end = date(d.year,d.month,d.day)
# 종목 코드 
# 삼성전자 : 005930.KS
# 애플 : AAPL

# 종목코드
itemCode1 = ''
itemCode2 = ''
# 종목 데이터 받아오기
stock1_df = data.DataReader("AAPL","yahoo",start, end) # start ~ end 까지
stock2_df = data.DataReader("AMD","yahoo",start, end) # start ~ end 까지

result = sm.ols(formula="score ~ iq + academy +game+ tv", data=df).fit()


stock1_df.plot()


plt.show()

