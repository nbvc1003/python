import pymongo, sys
import pandas as pd

# sample collection name stocks
# name : ['다음','네이버','넥슨','NC'
# price : 5030, 51100, 32000, 4000 생성
# mongo4 읽어서 주가 합계 , 주가 평균 출력


list = []
try:
    con = pymongo.MongoClient('127.0.0.1', 27017)
    db = con.sample
    # list = list(db.stocks.find())
    print(type(list))
    print(type(db.stocks.find()))
    for i in db.stocks.find():
        list.append(i)

except:
    print('애러 ', sys.exc_info())
else:
    print('입력성공')
finally:
    con.close()

df = pd.DataFrame(list, columns=['name','price'])
print(df)
print('합계 ',df['price'].sum())
print('평균 ',df['price'].mean())
