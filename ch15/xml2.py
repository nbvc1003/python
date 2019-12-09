from bs4 import BeautifulSoup
import urllib.request as req
import os.path

print("보고 싶은 지역을 입력하세요")
# 지역 코드 : 전국 108, 강원도 105,
stdId = input()
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId="+ stdId

savename = 'forcast.xml'

if not os.path.exists(savename):
    req.urlretrieve(url, savename) # 인터넷에서 다운받아서 파일로 저장
xml = open(savename, 'r',encoding='utf-8').read()
soup = BeautifulSoup(xml, 'html.parser')

info = {}
for location in soup.find_all('location'):
    name = location.find('city').string
    datas = location.find('data')
    data_wf = {}
    for data in datas:
        tmEf = data.find('tmEf').string
        wf = data.fine('wf').string
        # if not (tmEf in data_wf):
        #     info[tmEf] = [wf]
        data_wf[tmEf].append(wf)
    info[name].append(data_wf)

print(info)

# for name in info.keys():
#     print('+',name)
#     for data_wf in info[name]:

