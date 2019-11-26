import pymysql, sys


try:
    print('부서코드')
    deptno = int(input())
    dname = input('부서명')
    loc = input('근무지')
    con = pymysql.connect(host='127.0.0.1', port=3306,user='root', passwd='mysql', db='test', charset='utf8')
    csr = con.cursor()
    csr.execute("insert into dept values (%d, '%s', '%s')" % (deptno, dname, loc))
    con.commit()
    print('입력성공')
except:
    print("에러:", sys.exc_info())
finally:
    con.close()