import pymysql, sys
import pandas as pd


list=[]
try:
    con = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                          passwd='mysql', db='test', charset='utf8')
    csr = con.cursor()
    csr.execute('select * from dept')
    data = csr.fetchall()
    for i in data:
        list.append(i)
    csr.close()

except:
    print('애러', sys.exc_info())

finally:
    con.close()

df = pd.DataFrame(list,  columns=['deptno','dname','loc'])
print(df)

