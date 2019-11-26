import sys, pymysql
try:
    print('살제할 사번 입력 :')
    empno = int(input())
    con = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='mysql', db='test', charset='utf8')
    csr = con.cursor()
    csr.execute('delete from emp where empno={}'.format(empno))
    con.commit()
    print('삭제완료')
except:
    print("에러발생",sys.exc_info())
finally:
    con.close()