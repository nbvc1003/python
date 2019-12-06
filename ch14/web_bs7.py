from bs4 import BeautifulSoup
import  urllib.request as req

##exchangeList > li.on > a.head.usd > div > span.value

url ="https://finance.naver.com/marketindex/?tabSel=exchange"
res = req.urlopen(url)
# html = res.decode("utf-8")
soup = BeautifulSoup(res, 'html.parser')
print(soup)
# div.head_info
price = soup.select_one("div.head_info > span.value").string
date = soup.select_one("div.graph_info > span.time").string
print("오늘 {}의 환율 :{}".format(date,price))

