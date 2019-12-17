import pandas as pd
import numpy as np
# date_str = ["2017, 1, 1", "2017, 1, 4", "2017, 1, 5", "2017, 1, 6"]
date_str = ["2017-1-1", "2017-1-4", "2017-1-5", "2017-1-6"] # date 포맷을 어느정도 유지해야 인식함

# 문자열을 DatetimeIndex (날자 인덱스) 로 변경
idx = pd.to_datetime(date_str)
print(idx, type(idx))

np.random.seed(123)

# randn 평균0 표준편차1 정규분포 4건 데이터 를 인덱스 idx에 적용하여 생성
s = pd.Series(np.random.randn(4), index=idx)
print(s)
