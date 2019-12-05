import sqlite3 , sys
import pandas as pd

filepath = 'test.sqlite'
sql = 'insert into items(name, price) values(?,?)'
data = [('망고',7700),('키위',4000),('복숭아',8000),('수박',6000)]
try:
    con = sqlite3.connect(filepath)
    csr = con.cursor()
    # 여러 데이터를 한번에 처리 하는 함수
    # 하나의 sql에 대입해서 처리
    csr.executemany(sql,data)
    con.commit()
    csr.execute('select * from items where price>=? and price<=?',(4000, 8000))
    items = csr.fetchall()
    list = []
    for i in items:
        list.append(i)
    csr.close()
except:
    print('에러 ', sys.exc_info())
finally:
    con.close()

df = pd.DataFrame(list, columns=['item_id','name','price'])
print(df)