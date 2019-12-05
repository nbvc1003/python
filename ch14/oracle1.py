import cx_Oracle, sys
import pandas as pd


list = []
try:
    con = cx_Oracle.connect('scott/tiger@127.0.0.1:1521/xe')
    csr = con.cursor()
    csr.execute('select * from emp order by sal desc')
    data = csr.fetchall()
    for i in data:
        list.append(i)

    csr.close()
except:
    print('애러 ', sys.int_info())
finally:
    con.close()

df = pd.DataFrame(list, columns=['empno','ename','job','mgr','hiredate','sal','comm','deptno'])
print(df)

