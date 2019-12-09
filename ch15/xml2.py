from bs4 import BeautifulSoup
import urllib.request as req
import os.path

print("보고 싶은 지역을 입력하세요")
# 지역 코드 : 전국 108, 강원도 105,
stdId = input()
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId="+ stdId

savename = 'forcast.xml'

# if not os.path.exists(savename):
req.urlretrieve(url, savename) # 인터넷에서 다운받아서 파일로 저장

xml = open(savename, 'r',encoding='utf-8').read()
soup = BeautifulSoup(xml, 'html.parser')

info = []
for location in soup.find_all('location'):
    city = {}
    name = location.find('city').string
    datas = location.findAll('data')
    times = []
    for data in datas:
        dt={}
        tmEf = data.select_one('tmEf').string
        wf = data.select_one('wf').string
        dt['tmEf'] = tmEf
        dt['wf'] = wf
        times.append(dt)

    city[name] = times # 딕셔너리 -> 딕셔너리 데이터
    info.append(city)

print(type(info),info )

for i in info: #  info (city(times(dt {}) )) # i = city{}
    # print(i.keys())
    # print(i.values())
    print(type(i))
    for j in i: # i : city.value == dt{}  # j = dt
        print('\n+',j.string)
        print(type(j))
        for k in i[j]: # .
            print(type(i))
            print(k)

