import pandas as pd
import numpy as np

from datetime import datetime

# dates = [datetime(2017, 1, 1), datetime(2017, 1, 4), datetime(2017, 1, 5),
#          datetime(2017, 1, 6), datetime(2017, 1, 8), datetime(2017, 1, 10)]

dates = [datetime(2017, 1, 1), datetime(2017, 1, 4), datetime(2017, 1, 5),
         datetime(2017, 1, 6), datetime(2017, 1, 8), datetime(2017, 1, 10),
        datetime(2017, 1, 11), datetime(2017, 1, 12), datetime(2017, 1, 13)]

print(type(dates))
# dates 날짜 형일경우 그대로 index 로 넣을수 있다.
ts = pd.Series(np.random.randn(9), index=dates)
print(ts)

print(ts[ts.index[2]])
print(ts['20170104'])

# 데이터를 묶어서 출력
print(ts['2017-01']) # 1월 데이터
print(ts['2017-01-04':'2017-01-08']) # 4일부터 8일까지
print(ts.truncate(before='2017-01-08')) # 8일 이전 삭제
print(ts.truncate(after='2017-01-08')) # 8일 이후 삭제