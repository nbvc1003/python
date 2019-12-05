import requests

url = 'http://www.naver.com'
data = requests.get(url)
print(data.text)

