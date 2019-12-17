import datetime

dt = datetime.datetime.now() # 현재시간 (로컬시간)

print(dt)
print(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond)
print('요일 :', dt.weekday()) # 0,1,2,3,4,5,6  : 월화수목금토일


# 문자형태를 날짜형 타입으로 변경..
dt1 = datetime.datetime.strptime("2019-11-30 11:32", '%Y-%m-%d %H:%M')

dt2 = datetime.datetime.strptime("2019-12-16 10:32", '%Y-%m-%d %H:%M')
# 날짜형간의 연산 가능
print(dt2 - dt1)

# 날짜형을 문자형으로
s = dt2.strftime('%Y/%m/%d %H>%M/%S ') # 원하는 형태의 문자열로 변환
print(s)