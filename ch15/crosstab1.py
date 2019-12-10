import pandas as pd

# crosstab 그룹의 빈도수를 표시하기 위한 함수 ..

df = pd.read_csv('tips.csv')
# print(pd.crosstab(df.sex, df.smoker)) #아래와 동일
print(pd.crosstab(df['sex'], df['smoker'], margins=True))

print('===========================================================')
# 성별, 요일별, 총계

print(pd.crosstab(df['sex'],df['day'], margins=True))


print('===========================================================')
# 3개 그룹적용시
print(pd.crosstab([df['sex'],df['day']],df['smoker'], margins=True))