import pandas as pd

#fruits = pd.read_csv('good.csv')
fruits = pd.read_csv('good.csv', header=None,
                     names=['과일명','갯수','가격'],
                     thousands=None)
# thousands = None,

print(fruits)

# fruits = pd.read_csv('good.csv', header=None,
#                      names=['과일명','갯수','가격'],
#                      thousands=',',sep=',')
# print(fruits)