import pandas as pd
import numpy as np

df = pd.read_csv('tips.csv')
# 기준이 두개 : 시간별, 성별
result = df['tip'].groupby([df['time'], df['sex']])
print(result)
print('===============================================================')
# 시간별, 성별 평균
result = result.mean().unstack()
result = result.replace(np.nan, '-')
print(result)
