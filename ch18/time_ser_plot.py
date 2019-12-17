import pandas as pd
import matplotlib.pyplot as plt

#  parse_dates=True 인덱스를 date형식이다, 인덱스 컬럼은 0번
close_px_all = pd.read_csv('stock_px.csv', parse_dates=True, index_col=0)

# close_px_all['AAPL'].plot()
# close_px_all['AAPL'].loc['1990'].plot() # 1990년도만
close_px_all['AAPL'].loc['1990-02':'1990-05'].plot() # 1990/2 ~ 1990/5 까지 주가만

# 참고 : 여러개를 한꺼번에 그리면 색깔로 구분해서 가장 범위가 큰 그래프위에 함께 그려 준다. 

plt.show()