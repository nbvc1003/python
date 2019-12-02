import pandas as pd
import numpy as np
s = pd.Series([9904312, 3448737, 2890451, 2466052], index=['서울','부산','인천','대구'])

# 인구 3000000이상 출력
# 인구 1000000이상 출력
# s의 평균
# s 나누기 1000000

print(s[s>3000000])
print(s[s>1000000])
print(np.mean(s))
print(s/1000000)


