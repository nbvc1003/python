import pandas as pd
import pymysql, sys
list = []

try:
    con = pymysql.connect(host='127.0.0.1',port=3306, user='root',passwd='mysql',db='test',charset='utf8')
    csr = con.cursor()
    csr.execute("select date, name, price , count from stock")
    data = csr.fetchall()
    for i in data:
        list.append(i)
except:
    print('error',sys.exc_info())
finally:
    con.close()

df = pd.DataFrame(list, columns=['date','name','price','count'])
print(df)
print('===========================================')
# date와 name 을 중심으로 나머지 데이터를 표로 만든다.
# 이때 date와 name에 같은 이름이 있으면 에러 발생
print(df.pivot('date','name'))
