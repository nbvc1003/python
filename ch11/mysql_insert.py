import pymysql, sys

# emp empno, ename, job, 7319, hiredate(오늘) sal, comm, deptno(10)
try:
    
    empno = int(input('사번'))
    ename = input('이름')
    job = input('업무')
    sal = int(input('급여'))
    # mysql 의 root / mysql 계정에 db : test 에 연결후 작업
    con = pymysql.connect(host='127.0.0.1', port=3306,user='root', passwd='mysql', db='test', charset='utf8')
    csr = con.cursor()
    csr.execute("insert into emp values (%d, '%s', '%s', 7369,"
                "current_date(), %d, 0,10)"%(empno, ename, job, sal))
    con.commit() # 입력 수정 삭제시 메모리 내용을 실제 db에 반영시킬때 사용
    print('입력성공')
except:
    print("에러:", sys.exc_info())
finally:
    con.close()