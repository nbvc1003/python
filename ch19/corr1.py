import pandas as pd

sales = pd.Series([3,5,8,11,13])
dms = pd.Series([1,2,3,4,5])

print('상관계수 :', sales.corr(dms)) # 값이 1에 가까우면 서로 관련이 높다.

