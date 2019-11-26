import sys, pymysql

try:
    deptno = int(input('부서코드'))
    dname = input('이름')
    loc = input('근무지')

    con = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='mysql', db='test', charset='utf8')
    csr = con.cursor()
    csr.execute("update dept set dname='%s', loc='%s' where deptno = %d "
                % (dname, loc, deptno))

    con.commit()
    print('수정완료')
except:
    print('에러 :', sys.exc_info())

finally:
    con.close()
