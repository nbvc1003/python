import pandas as pd

df = pd.read_csv('tips.csv')
result = df.groupby('sex')

# 항목별 다른 함수를 적용한다. (tip, size 각다른 함수 적용)
print(result.agg({'tip':['mean','sum'],'size':'mean','total_bill':'sum'}))
