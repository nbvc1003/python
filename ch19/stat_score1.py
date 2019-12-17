import pandas as pd

df = pd.read_csv('student.csv', encoding='euc-kr')

# 이름 을 index로
df.index = df['이름']
print(df)

# 이름 컬럼 삭제
df = df.drop('이름', axis=1)
print(df)

kor_mean = df['국어'].mean()
eng_mean = df['영어'].mean()
math_mean = df['수학'].mean()

#표준편차 구하기
kor_std = df['국어'].std()
eng_std = df['영어'].std()
math_std = df['수학'].std()

# 표준점수 == (값 - 평균) / 표준편차
df['국어표준점수'] = round((df['국어'] - kor_mean) / kor_std, 2)
df['영어표준점수'] = (df['영어'] - eng_mean) / eng_std
df['수학표준점수'] = (df['수학'] - math_mean) / math_std
# print(df)

# 편차점수 = 표준점수 * 10 + 50
df['국어편차점수'] = df['국어표준점수'] * 10 + 50
df['영어편차점수'] = df['영어표준점수'] * 10 + 50
df['수학편차점수'] = df['수학표준점수'] * 10 + 50

print(df)
