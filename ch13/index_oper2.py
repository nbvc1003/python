import pandas as pd

fruit = pd.Series([4000, 3000, 3500, 2000], index=['apple','mellon','orange','kiwi'])

fruit2 = pd.Series([4300, 3200, 3600, 2100], index=['apple','mellon','tomato','kiwi'])

# ds = fruit - fruit2
ds = fruit2 - fruit
print(ds)
# fruit.values - fruit2.values
print(fruit2.values - fruit.values)
# ds 가 notnull 인경우만 출력
print(ds[pd.notnull(ds)])
