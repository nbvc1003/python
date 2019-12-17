import pandas as pd
import numpy as np

# date_range 지정된 기간의 날짜 인덱스를 한번에 생성해준다.
print(pd.date_range('2019-4-1','2019-4-30'), type(pd.date_range('2019-4-1','2019-4-30')))

print(pd.date_range(start='2019-4-1', periods=30)) # 4-1 부터 30일 생성
print(pd.date_range(start='2019-4-1', periods=30, freq='B')) # 근무날짜만 포함해서 30일 생성 (토일,휴일 제외)

print(pd.date_range('2019-4-1', '2019-12-31', freq='MS')) # MS (Month Start) : 월초 값만
print(pd.date_range('2019-4-1', '2019-12-31', freq='M')) # MS (Month Start) : 월말 값만

# 2000/1/1 기준으로 월말 4개를 생성
ts = pd.Series(np.random.randn(4), index= pd.date_range("2000-1-1", periods=4, freq='M'))

print(ts)

# shift : 데이터를 인덱스 기준으로 이동 시킨다.
print(ts.shift(1)) # 앞쪽으로 이동
print(ts.shift(-1)) # 뒤쪽으로 이동

# data는 그대로 이고 index 값이 변경된다.
print(ts.shift(1, freq='M')) # 모든 인덱스 날짜가 한달씩 뒤로 변경된다.