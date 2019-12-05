import pymongo,sys
import pandas as pd

try:
    con = pymongo.MongoClient('127.0.0.1',27017)
    db = con.sample # sample 이름의 db로 이동 없으면 생성 
    
    # fruits 테이블 이 없으면 생성
    db.fruits.insert_one({'name': 'apple' , 'count':10,'price':1500})
    db.fruits.insert_one({'name': 'banana' , 'count':4,'price':500})
    db.fruits.insert_one({'name': 'orange', 'count': 13, 'price': 1000})
    db.fruits.insert_one({'name': 'kiwi', 'count': 22, 'price': 1300})
    db.fruits.insert_one({'name': 'melon', 'count': 16, 'price': 2500})
    db.fruits.insert_one({'name': 'mango', 'count': 4, 'price': 550})

except:
    print('애러 ', sys.int_info())
else:
    print('입력성공')
finally:
    con.close()


