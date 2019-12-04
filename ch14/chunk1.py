import pandas as pd

# chunksize = 3 -> 데이터를 한번에 읽어오는 양
goods = pd.read_csv('good.csv', header=None, chunksize=3)

print('----------------------------------------------')
for i in goods:
    # 묶여 있는 값들 범위안에서 정렬 by = 정렬기준컬럼명
    print(i.sort_values(by=2, ascending=False))
    print('=========================')

