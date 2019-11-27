import cx_Oracle, sys

try:
    deptno = int(input('부서 코드 '))
    dname = input('부서명 ')
    loc = input('근무지 ')
    con = cx_Oracle.connect('scott/tiger@127.0.0.1:1521/xe')
    csr = con.cursor()
    sql = "update dept set dname='{}', loc='{}' where deptno={}"
    csr.execute(sql.format(dname, loc, deptno))
    con.commit(); csr.close()
    print("수정 성공")

except:
    print('애러', sys.exc_info())
finally:
    con.close()