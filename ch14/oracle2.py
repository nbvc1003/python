# salgrade : grade, losal, hisal
# dataframe 저장 / 출력

import cx_Oracle, sys
import pandas as pd

list=[]
try:
    con = cx_Oracle.connect('scott/tiger@127.0.0.1:1521/xe')
    csr = con.cursor()
    csr.execute('select * from salgrade')
    data = csr.fetchall()
    for i in data:
        list.append(i)
    csr.close()
except:
    print("애러 ", sys.int_info())
finally:
    con.close()

df = pd.DataFrame(list, columns=['grade','losal','hisal'])
print(df)



