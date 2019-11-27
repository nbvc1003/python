import cx_Oracle,sys

try:
    empno = int(input('사번 '))
    ename = input('이름 ')
    sal = int(input('급여 '))
    con = cx_Oracle.connect('scott/tiger@127.0.0.1:1521/xe')
    csr = con.cursor()
    sql = "update emp set ename='%s', sal=%d where empno=%d"
    csr.execute(sql % (ename, sal, empno))
    con.commit()
    csr.close()
    print('수정 완료')
except:
    print('error ', sys.exc_info())
finally:
    con.close()