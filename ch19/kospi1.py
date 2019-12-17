from pandas_datareader import data
from datetime import date


d = date.today()

start = date(2019,1,1)
end = date(d.year,d.month,d.day)

# yahoo finance에서 코스피 심볼은 ^KS11이다.
imsi = data.DataReader("^KS11","yahoo",start, end) # start ~ end 까지
# 구글에서 가져 올때
# imsi = data.DataReader("KRX:KOSPI","google",start,end)

imsi = imsi.sort_index(ascending=False) # 최신을 앞쪽으로 
s = imsi['Close'] # 종가만
li = []
for i in range(0, 30):
    li.append(s[i])
print(li)