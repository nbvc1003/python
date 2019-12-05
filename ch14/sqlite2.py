import sqlite3, sys
import pandas as pd

try:
    dbpath = 'test.sqlite'
    # python에 설치되어 있는 기본 sqlite db 에 연결된다.
    con = sqlite3.connect(dbpath)
    csr = con.cursor()
    list = []
    data = csr.execute('select * from items')
    for i in data:
        list.append(i)
    csr.close()

except:
    print('에러 ',sys.exc_info())
finally:
    con.close()

df = pd.DataFrame(list, columns=['item_id','name','price'])
print(df)