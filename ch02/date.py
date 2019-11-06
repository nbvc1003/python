

# 오늘은 2016년 12월 25일 입니다.
year = 2016
month = 12
day = 25
week = "일요일"

#문자와 숫자를 함께 사용하기 위하여
#print("오늘은 " +year+"년"+month+"월" +day+"일"+week+"입니다.")
print("오늘은 "+str(year)+"년"+str(month)+"월" +str(day)+"일"+str(week)+"입니다.")
print("오늘은 {}년 {}월 {}일 {}입니다.".format(year,month,day,week))
print("오늘은 %d년 %d월 %d일 %s입니다."%(year,month,day,week))

