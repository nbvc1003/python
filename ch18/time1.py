import time

print('안녕')
time.sleep(2) # 초단위로 sleep 기능
print('친구들')

print(time.time()) # 1970년 1/1/ 부터 누적된 시간 (epoch time)
print(time.gmtime()) # utc time 글로벌 표준시 (우리나라시간과 9시간 차이) (세슘 진동수 기준 :1972년 부터 시행)
print(time.localtime()) # 현재 지역 시간 == 표준시 + 9 hour





