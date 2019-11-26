import sys, pymysql
try:
    deptno = int(input('부서코드? '))
    con = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='mysql',db='test', charset='utf8')
    csr = con.cursor()
    csr.execute('select * from dept where deptno = %d' % (deptno))
    data = csr.fetchone() # 데이터 1건 가져오기.
    for imsi in data:
        print(imsi)
    print(data)
except:
    print('에러', sys.exc_info())

finally:
    con.close()