import urllib.request as req
import os.path, random, json
import pandas as pd

url = 'https://api.github.com/repositories'
savename = "repo.jason"

if not os.path.exists(url):
    req.urlretrieve(url, savename)

# load : file로부터 json데이터 가져 오기

## 1번째 방법
# load : file로 부터 json데이터 가져 오기
items = json.load(open(savename, 'r', encoding='utf-8'))

## 2번째 방법
## loads : text파일을 json형식으로 해석
# s = open(savename, 'r', encoding='utf-8').read()
# items = json.loads(s)

for item in items:
    print((item["name"]+" - "+ item["owner"]["login"]))

for item in items:
    # 숫자형과 문자형의 + 연산 안됨
    print(str(item["id"])+" - "+item["owner"]["node_id"])