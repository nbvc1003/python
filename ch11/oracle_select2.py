import cx_Oracle, sys
try:
    deptno = int(input('조회할 부서코드 입력 : '))
    # 오라클 db연결
    con = cx_Oracle.connect('scott/tiger@127.0.0.1:1521/xe')
    csr = con.cursor()

    csr.execute("select * from dept where deptno={}".format(deptno))

    data = csr.fetchone()

    for imsi in data:
        print(imsi)

    print(data)
    csr.close()

except:
    print("애러 ", sys.exc_info())
finally:
    con.close()