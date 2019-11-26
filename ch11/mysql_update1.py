import pymysql, sys

# emp empno, ename, job, 7319, hiredate(오늘) sal, comm, deptno(10)
try:

    empno = int(input('사번'))
    ename = input('이름')
    job = input('업무')
    sal = int(input('급여'))
    # mysql 의 root / mysql 계정에 db : test 에 연결후 작업
    con = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='mysql', db='test', charset='utf8')
    csr = con.cursor()
    csr.execute("update emp set ename='%s', job='%s', sal=%d "
                "where empno=%d" % (ename, job, sal, empno))
    con.commit()
    print('성공')
except:
    print("에러:", sys.exc_info())
finally:
    con.close()