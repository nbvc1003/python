import pandas as pd

items = pd.read_csv('fruit.csv', header=None,
                    sep='|', names=['과일명','수량','가격'])

print(items)
