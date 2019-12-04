from pandas import Series, DataFrame
import pandas as pd
import numpy as np
stocks = {'2017-02-19':{'다음':50300,"네이버": 51100, "넥슨":32000, "NC":4000},
        "2017-02-22":{'다음':50300, '네이버': 50800, "넥슨":35000, "NC":6500},
        '2017-02-23':{'다음':50800,'네이버': 50700, "넥슨":37000, "NC":8000}}
data = DataFrame(stocks)
data = data.T
d = data.pct_change().fillna(0)
print(d)
print('==================')
# 값이 1 에 가까울수록 연관성이 높음..
print('넥슨과 네이버 (상관관계)', d.넥슨.corr(d.네이버))
print('==================')
print('넥슨과 NC (상관관계)', d.넥슨.corr(d.NC))
print('==================')
print(d.corr()) # 전체 관계를 표로
print('==================')
print(d.corrwith(d.NC)) # 특정 변수와의 상관관계 값들..

