import pandas as pd

fruit = pd.Series([4000, 3000, 3500, 2000], index=['apple','mellon','orange','kiwi'])

# index 1, mallon data출력
# index 1, mallon 인덱스 +데이터
# index 1 :3
# index mellon : kiwi
# 4000작고 2000큰데이터

print(fruit[1])
print(fruit['mellon'])
print('===============================')
print(fruit[[1]])
print(fruit[['mellon']])
print('===============================')
print(fruit[1:3])
print(fruit['mellon':'kiwi'])
print('===============================')
print(fruit[(fruit < 4000) & (fruit > 2000)])
print('===============================')
print(fruit.apple, fruit.orange)

