from bs4 import BeautifulSoup
import requests

req = requests.get("https://beomi.github.io/beomi.github.io_old/")
html = req.text
print(html)

head = req.headers
stat = req.status_code
# 200 정상,
# 440 : Not Found
# 500 : Error
print(stat)

soup = BeautifulSoup(html, 'html.parser')


