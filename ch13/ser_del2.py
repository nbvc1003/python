import pandas as pd

fruit = pd.Series([4000, 3000, 3500, 2000],
                  index=['apple','blueberry','orange','kiwi'])

# banana 2500 추가
# apple 4200
# kiwi 삭제

fruit["banana"] = 2500
fruit["apple"] = 4200
print(fruit)
del fruit["kiwi"]
print(fruit)
# 3000 이상만 출력
print(fruit[fruit >= 3000])

