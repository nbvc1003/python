import sys, pymysql
try:
    print('삭제할 부서코드 입력 :')
    deptno = int(input())
    con = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='mysql', db='test', charset='utf8')
    csr = con.cursor()
    csr.execute('delete from dept where deptno={}'.format(deptno))
    con.commit()
    print('삭제완료')
except:
    print("에러발생",sys.exc_info())
finally:
    con.close()