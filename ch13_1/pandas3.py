import pandas as pd
good1 = pd.Series([4000, 3500, None, 2000],
                  index=['apple','mango','orange','kiwi'])

good2 = pd.Series([3000, 3000, 3500, 2000],
                  index=['apple','banana','mango','kiwi'])

print(pd.isnull(good1)) # 값이 없는지 여부
print(pd.notnull(good1)) # 값이 있는지 여부 

print(good1+good2) # 양쪽에 다 있으면 연산결과값 한쪽만 있으면 NaN

print(good1[1])
print(good2['apple'])
print(good1[1] + good2['apple'])

# good1 apple, mango, kiwi
# good2 index 0, 2 ,3
print('---------------------------------------------')
print(good1['apple'], good1['mango'], good1['kiwi'])
print(good2[0],good2[2],good2[3])