
import pandas as pd


stocks = {
        '2017-02-19':{'다음':50300,"네이버": 51100, "넥슨":None, "NC":None},
        "2017-02-22":{'다음':50300, '네이버': 50800, "넥슨":35000, "NC":None},
        '2017-02-23':{'다음':50800,'네이버': 53000, "넥슨":37000, "NC":8000}}

data = pd.DataFrame(stocks).T
print(data)

# 컬럼명 : 날자 , 다음 , 네이버 -> stock.csv 저장

data.index.name = '날짜'
data = data.reset_index()
print(data)
data.to_csv('stock.csv',index=False)
# 해더 제거 후 저장
data.to_csv('stock.csv',header=False, index=False)