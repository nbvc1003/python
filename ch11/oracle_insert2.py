import cx_Oracle, sys
try:
    deptno = int(input('부서코드 '))
    dname = input('부서명')
    loc = input('근무지 ')

    con = cx_Oracle.connect('scott/tiger@127.0.0.1:1521/xe')
    csr = con.cursor()
    csr.execute("insert into dept values({},'{}','{}')".format(deptno,dname,loc))
    con.commit()
    csr.close()
    print('입력완료')
except:
    print("error ", sys.exc_info())
finally:
    con.close()