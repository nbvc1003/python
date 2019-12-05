import sqlite3, sys
import pandas as pd

dbpath = 'test.sqlite' # 파일 이름처럼 생성
sql = 'insert into items (name,price) values(?,?)'
list = []
try:
    con = sqlite3.connect(dbpath)
    csr = con.cursor()
    while True:
        print('과일명 :?')
        name = input()
        if name == 'x': break;
        print('가격?')
        price = int(input())
        csr.execute(sql, (name, price)) # 입력받은 name, price 를 입력한다.
        con.commit()
    csr.execute('select * from items')
    items = csr.fetchall()
    for i in items:
        list.append(i)
    csr.close()
except:
    print('에러 ', sys.exc_info())
finally:
    con.close()


df = pd.DataFrame(list, columns= ['item_id','name','price'])
print(df)





