import pandas as pd

df = pd.read_csv('tips.csv')
result = df.groupby('sex')

# 숫자로된 컬럼을 찾아서 함수 적용
print(result.agg([('평균','mean'),('합계','sum')]))
