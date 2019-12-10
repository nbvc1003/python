import pandas as pd
import pymysql , sys

# mysql , emp 부서/ 업무별 급여 합계 pivot
list = []
try:
    con = pymysql.connect(host='127.0.0.1',port=3306, user='root',passwd='mysql',db='test',charset='utf8')
    csr = con.cursor()
    # (deptno, job) 의 복합키를 가지는 형태의 표로 조회
    csr.execute("select deptno, job, sum(sal) from emp group by deptno, job order by deptno, job")
    data = csr.fetchall()
    for i in data:
        list.append(i)
except:
    print('error:',sys.exc_info())
finally:
    con.close()


df = pd.DataFrame(list, columns=['deptno','job','sal_sum'])
print(df)
print('=================================================')
print(df.pivot('deptno','job'))

