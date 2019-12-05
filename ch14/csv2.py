import pandas as pd

#fruits = pd.read_csv('good.csv')
fruits = pd.read_csv('good.csv', header=None,
                     names=['과일명','갯수','가격'],
                     ) #thousands=',')
# thousands = None -> 숫자데이터에 천자리 구분 하는 ',' 이 있을경우 무시하고 처리하도록 하는 목적 
# 현재 동작 제대로 안됨
print(fruits)

# fruits = pd.read_csv('good.csv', header=None,
#                      names=['과일명','갯수','가격'],
#                      thousands=',',sep=',')
# print(fruits)