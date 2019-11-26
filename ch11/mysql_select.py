import sys, pymysql
try:
    empno = int(input('사번? '))
    con = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='mysql',db='test', charset='utf8')
    csr = con.cursor()
    csr.execute('select * from emp where empno = %d' % (empno))
    # con.commit()
    data = csr.fetchone()
    for imsi in data:
        print(imsi)

except:
    print('에러', sys.exc_info())

finally:
    con.close()