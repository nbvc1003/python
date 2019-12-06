from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests
from lxml.html import parse
from io import StringIO

url = "https://finance.naver.com/item/sise_day.nhn?code=005930"

data = requests.get(url)
doc = parse(StringIO(data.text)) # 데이터가 계층형 구조로
root = doc.getroot() # 최상위 테그 html
tables = root.findall(".//table") # table 테그 전부 가져온다.
titles = tables[0].findall(".//th") # [0]에서 th 태그를 전부 가져 온다.
cols = []

for title in titles:
    # print(title.text_content())
    cols.append(title.text_content()) # title 테그 에 있는 text정보를 받아온다.

values = []
contens = tables[0].findall('.//td') # 하위 td 엘리맨트 전부 가져 온다.
for con in contens:
    if con.text_content() != '': # 값이 있으면
        values.append(con.text_content().strip())

ar = np.array(values).reshape(10,7)
df = pd.DataFrame(ar, columns=cols)
print(df)




