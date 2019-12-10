# 성별, 흡연  tip평균 NaN은 -

import pandas as pd
import numpy as np

df = pd.read_csv('tips.csv')
print(df)
gp = df['tip'].groupby([df['sex'],df['smoker']])
print(gp.mean())
print('=====================================================')
#            평균,  2차인덱스를 컬럼으로
result = gp.mean().unstack().replace({np.nan:'-'})
print(result)

