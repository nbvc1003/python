import pandas as pd

data = {
"국어": [80, 90, 70, 30],
"영어": [90, 70, 60, 40],
"수학": [90, 60, 80, 70],
}
columns = ["국어", "영어", "수학"]
index = ["춘향", "몽룡", "향단", "방자"]

df = pd.DataFrame(data, index=index , columns=columns)
print(df)
df1 = df.reindex(['춘향','몽룡','제니','하니'])
print(df1)
# NaN 을 0으로
df1 = df.reindex(['춘향','몽룡','제니','하니'], fill_value=0)
print(df.index, df1.index)
# 먼저 위치에 있던 값 사용

# print(df1)
# 제니 = [67,78,88]
df1.loc['제니'] = [67,78,88]
df1.loc['하니'] = [55,77,47]
print(df1)

# method='ffill' 같은 DataFrame에 적용됨..
# index 값이 연속되는 값을 사용 할경우 유효 순서를 특정하기 어려울경우 오류
# method='ffill' -> index 값에는 숫자 or 알파벳 과 같은 순서를 특정할수 있는 데이터형식으로 되어있을 경우 만 사용
df1 = df1.reindex(['춘향','몽룡','제니','하니'], method='ffill')

print(df1)

