import pandas as pd

# fruits = pd.read_csv('good.csv')
fruits = pd.read_csv('good2.csv', header=None,
                     names=['과일명', '갯수', '가격'],
                     thousands='a', sep=':')

print(fruits)