import math
import pandas as pd
s = pd.Series([10,11,10.78])

# pct_change (뒤 숫자 - 앞숫자)/ 앞숫자
# computer에서 실수는 부동 소수점으로 표현
print('산술 평균 성장율 :', s.pct_change().mean())

print('기아 평균 성장율 :', math.sqrt((11/10) * (10.78/11)))

print('산술 평균 속도 :', (100+60)/2)
print('조화 평균 속도 :', 2*100*60/(100+60))
