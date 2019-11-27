import cx_Oracle, sys

try:
    print('삭제할 사번을 입력 하세요')
    empno = int(input())
    con = cx_Oracle.connect('scott/tiger@127.0.0.1:1521/xe')
    csr = con.cursor()
    csr.execute("delete from emp where empno={}".format(empno))
    con.commit()
    csr.close()
    print('삭제성공')
except:
    print('error', sys.exc_info())
finally:
    con.close()