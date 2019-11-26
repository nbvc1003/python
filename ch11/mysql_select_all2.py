import pymysql, sys
try:

    con = pymysql.connect(host='127.0.0.1', port=3306,
                          user='root',passwd='mysql', db='test', charset='utf8')
    csr = con.cursor()
    csr.execute("select * from dept order by deptno")
    data = csr.fetchall()
    for imsi in data:
        print(imsi)

except:
    print('에러 :', sys.exc_info())

finally:
    con.close()