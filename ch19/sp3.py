from scipy import stats
import scipy as sp
import pandas as pd
import numpy as np

items = pd.read_csv('tdata.csv', encoding='utf-8')
print(items)
# 평균이 75 이냐  아니냐 가설 (유의 수준 5%)
items['성적'] = items['성적']/75 - 1

# 검정 통계량
# ddof=1 자유도
t = items['성적'].mean()/items['성적'].std(ddof=1)*np.sqrt(len(items['성적']))

print('검정 통계 :', t)

# sp.stats.t  student 랜덤변수
# sp.stats.t(df= len(items['성적'])-1).cdf(t) -> 귀무가설이 맞지 않을 확률
result = 1- sp.stats.t(df= len(items['성적'])-1).cdf(t)
print('유의확율 :', result)

if result >= 0.05:
    print('평균이 75 라는 귀무가설 채택')
else:
    print('평균이 75 라는 귀무가설 기각')