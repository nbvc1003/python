import pymongo, sys
import pandas as pd


try:
    con = pymongo.MongoClient('127.0.0.1', 27017)
    db = con.sample
    list = list(db.fruits.find({}))
except:
    print('애러 ', sys.exc_info())
else:
    print('성공')
finally:
    con.close()

print(type(list))
df = pd.DataFrame(list,columns=['name','count','price'])
print(df)
print('합계:',df['count'].sum())
print('평균:',df['price'].mean())
