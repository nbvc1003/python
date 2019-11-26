import sys, cx_Oracle

try:
    con = cx_Oracle.connect('scott/tiger@127.0.0.1:1521/xe')
    csr = con.cursor()
    csr.execute("select * from dept order by deptno ")
    data = csr.fetchall()
    for imsi in data:
        print(imsi)
    print(data)
    csr.close()

except:
    print('에러', sys.exc_info())
finally:
    con.close()