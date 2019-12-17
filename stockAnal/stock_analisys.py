from pandas_datareader import data
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats, polyval


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 차트에 한글 가능하도록
from matplotlib import font_manager, rc, rcParams
font_name = font_manager.FontProperties(
    fname="c:/windows/Fonts/malgun.ttf").get_name()
rc('font',family=font_name)
rcParams['axes.unicode_minus'] = False # 부호표시 (-,+) 사용할때
###
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


## 입력 받을 데이터
# 종목 코드 2개
# 시작 날짜와 끝 날짜 .
# 분석 시작 버튼 이벤트.
#

d = date.today()
start = date(2019,1,1)
end = date(d.year,d.month,d.day)
# 종목 코드 
# 삼성전자 : 005930.KS
# 애플 : AAPL

# 종목코드
targetStockCode = 'targetStockCode'
compStockCode = 'compStockCode'
# 종목 데이터 받아오기
targetStock_df = data.DataReader("AAPL", "yahoo", start, end) # start ~ end 까지
compStock_df = data.DataReader("AMD", "yahoo", start, end) # start ~ end 까지
tsd = targetStock_df['Close']
csd = compStock_df['Close']
slope, intersecept, r_value, p_value, stderr = stats.linregress(tsd, csd)

print(tsd)
print(csd)

print('기울기 :', slope)
print('절편 :', intersecept)
print('상관계수 :', r_value)
print('유의수준 :', p_value)

#
ry = polyval([slope, intersecept],tsd)
plt.plot(tsd, csd, 'k.')
plt.plot(tsd, ry, 'r')
plt.title('{}/{}'.format(targetStockCode, compStockCode))
plt.xlabel(targetStockCode)
plt.ylabel(compStockCode)
plt.legend(['price','polyval'])
plt.show()


# stock1_df.plot()


# plt.show()

