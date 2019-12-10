import pandas as pd

df = pd.read_csv('tips.csv')

# 각항목별로 함수를 적용한다.
print(df[['total_bill','tip','size']].apply('sum'))
print(df[['total_bill','tip','size']].apply('mean'))
# 함수 여러개 적용할때 리스트 형식으로 
print(df[['total_bill','tip','size']].apply(['mean','sum','count']))
print(df[['tip','size']].apply(['mean','sum','count']))