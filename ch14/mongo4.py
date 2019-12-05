import pymongo, sys
import pandas as pd



stocks = {'2017-02-19':{'다음':50300,"네이버": 51100},
        "2017-02-22":{'다음':50300, '네이버': 50800},
        '2016-02-23':{'다음':50800,'네이버': 53000}}


try:
    con = pymongo.MongoClient('127.0.0.1',27017)
    db = con.sample
    db.stocks.drop() # 기존의 stocks collection이 있다면 삭제한다.
    # stocks collections을 만들고 그안에 데이터를 넣는다.
    db.stocks.insert_one({'name': '다음','price':50300})
    db.stocks.insert_one({'name': '네이버', 'price': 51100})
    db.stocks.insert_one({'name': '넥슨', 'price': 32000})
    db.stocks.insert_one({'name': 'NC', 'price': 4000})

    
except:
    print('애러 ', sys.exc_info())
else:
    print('입력성공')
finally:
    con.close()



