import cx_Oracle, sys
try:
    empno = int(input('사번 '))
    ename = input('이름 ')
    job = input('업무 ')
    sal = int(input('급여'))
    con = cx_Oracle.connect('scott/tiger@127.0.0.1:1521/xe')
    csr = con.cursor()
    csr.execute("insert into emp values({},'{}','{}', 7369, sysdate,{}, 0, 10)".format(empno, ename, job, sal))

    con.commit()
    csr.close()
    print("입력 성공 ")
except:
    print("에러 ",sys.exc_info())
finally:
    con.close()