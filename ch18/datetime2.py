import datetime

dt = datetime.datetime.now()
# datetime 형 에는 date + time 두 타입이 함께 있다.
print('날짜 :',dt.date())
print('시간 :',dt.time())

# 날짜만 입력해서 date 객체 생성
d = datetime.date(2019,12,16)
print(d, type(d))

# 시간만 입력해서 time 객체 생성
t = datetime.time(11, 3, 17)
print(t, type(t))

#  combine : date + time  합칠때 사용
print(datetime.datetime.combine(d,t))

# 날짜와 시간을 함께 입력해서 datetime 객체를 생성
dt1 = datetime.datetime(2019, 12,25,12,25,14)
dt2 = datetime.datetime(2019, 12,16,12,16,14)
print(dt1, dt2, type(dt1), type(dt2))
print('크리스마스까지 남은시간 :',dt1-dt2)
print((dt1-dt2).days)






