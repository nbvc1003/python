import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# , 를 업애는 함수
def f(st): # 
    #  , 로 문자열을 나눠 배열로 만들고
    # 이때 , 가 사라진다.
    # 다시 k 변수에 합쳐서 리턴
    st = str(st)
    ar = st.split(',')
    k = ''
    for i in ar:
        k = k+i
    return k

# 문사를 실수로 바꾸는 함수
def func(st):
    st = str(st)
    return float(st)

stockItem = '005930' # 삼성전자 기업코드
datelist = [] # 날짜
samsunglist = [] # 주가리스트

# 1 ~3 페이지 까지
for i in range(1,4):# i = 1,2,3
    url = "https://finance.naver.com/item/sise_day.nhn?code="+\
          stockItem+"&page="+str(i)
    html = urlopen(url)
    source = BeautifulSoup(html.read(),'html.parser')
    # print(source)
    srlists = source.find_all("tr")
    time.sleep(1.5)
    # print(len(stlist))
    for j in range(1, len(srlists)-1):
        if srlists[j].span != None: # span 테그가 있는 데이터 제외하고
            datelist.append(srlists[j].td.text)
            samsunglist.append(srlists[j].find_all("td", class_="num")[0].text)
            # td 테그 class 값이 num 인 값들중 0번째 text 값


df = pd.Series(samsunglist)
# map : 함수, Series 등의 조건 인자를 받아서 새로운 Series 객체를 생성한다.
df = df.map(f) # , 제거
# print(df)
df = df.map(func) # 문자가 실수로
print(df)






