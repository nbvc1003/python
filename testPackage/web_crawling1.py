from bs4 import BeautifulSoup # XML, HTML
import urllib.request as req

url = "http://www.inven.co.kr/board/destinyguardians/5051"
res = req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')

# ###
#listDic = {}
# # 게시물 단위로 검색
# bbslist = soup.select("div#powerbbsBody")
#
# for item in bbslist:
#     # 각 게시물 단위로 요소 분리해서 검색
#
#     date = item.select_one("td.date").string
#     subject = item.select_one("td.bbsSubject > a.sj_ln").string
#
#     if date != None and subject != None:
#         listDic[str(date).strip] = str(subject).strip()
#
# print(listDic)
# ###

bbsListDic = {}
bbsNo = 0
bbs = soup.select_one("div#powerbbsBody")
listItems = bbs.select("tr.ls")
print(len(listItems))
for item in listItems:
    itemNo = str(item.select_one(".bbsNo").string).strip()
    itemSub = str(item.select_one(".bbsSubject > a.sj_ln").string).strip()
    if itemNo.isdigit():
        # print(itemNo, itemSub)
        bbsListDic[itemNo] = itemSub

print(len(bbsListDic),bbsListDic)



# num = bbs.select(".bbsNo")
# for i in num:
#     num2 = str(i.string)
#     if num2.isdigit():
#         print(num2)




