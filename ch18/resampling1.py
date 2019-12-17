import pandas as pd
import numpy as np

# 1/1 부터 분단위로 30개 생성
ran = pd.date_range('1/1/2017', periods= 30, freq='T') # freq='T' 분단위
print(ran)

# 인덱스가 2017-1-1 00:01:00 ~ 2017-1-1-1 00:30:00 이고 데이터 0 ~ 30 인 Series
ts = pd.Series(np.arange(30), index=ran)
print(ts)

# 10분 단위 합계 ( 'M' 월단위)
print(ts.resample('10T').sum()) # 10분씩 합계 데이터로 생성
print(ts.resample('10T', label='left').sum()) # 인덱스(10분의)에 앞쪽값을 사용한다. (디폴트)
print(ts.resample('10T', label='right').sum()) # 인덱스(10분의)에 뒤쪽 값을 사용한다.

# 날짜단위의 index 150개 생성
ran1 = pd.date_range('2019/1/1',periods=150, freq='D')
ts1 = pd.Series(np.arange(150), index=ran1) # 0 ~ 150 value 생성
print(ts1)

def mo(x): # 원 데이터에서 월만 반환
    # print(type(x))
    return x.month

#월별 합계 구하기

# 월단위 합계
print(ts1.resample('M').sum())

print(ts1.groupby(mo).sum())
print(ts1.groupby(ts1.index.month).sum()) # 위와 동일하다.







