import pandas as pd
import xml.etree.ElementTree as ET

import urllib.request
url = 'http://www.kma.go.kr/wid/queryDFS.jsp?gridx=%d&gridy=%d'
request = urllib.request.Request(url)

response = urllib.request.urlopen(request)

tree = ET.parse(response)
print(tree)

root = tree.getroot()
k = root.find("body")
print(k)

items = k.findall("data")
ar = []

for i in items:
    item = {}
    item['hour'] = i.find('hour').text
    item['temp'] = i.find('temp').text # temp 태그사이의 문자열
    item['wfKor'] = i.find('wfKor').text
    ar.append(item)

df = pd.DataFrame(ar, columns=['hour','temp','wfKor'])

print(df)
