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

keyword = input('검색 키워드 :')

bbsList = []
bbsNo = 0
bbs = soup.select_one("div#powerbbsBody")
listItems = bbs.select("tr.ls")
print(len(listItems))
for item in listItems:
    itemNo = str(item.select_one(".bbsNo").string).strip()
    itemDate = str(item.select_one(".date").string).strip()
    itemSub = str(item.select_one(".bbsSubject > a.sj_ln").string).strip()
    # 게이판리스트의 No값이 숫자인 게시물만 dic으로
    bbsListDic = {}
    if itemNo.isdigit() and itemDate.find(':'):
        # print(itemNo, itemSub)
        bbsListDic['id'] = int(itemNo)
        bbsListDic['date'] = itemDate
        bbsListDic['subject'] = itemSub
        bbsList.append(bbsListDic)

        if bbsNo < int(itemNo):
            bbsNo = int(itemNo)


print("가장최근 게시물 번호 : {}".format(bbsNo))
# print(len(bbsList),bbsList)
findList = []
for item in bbsList:

    if item['subject'].find(keyword) > 0:
        findList.append(item)
    if len(findList) > 5 :
        break;

if len(findList) > 0:
    print(findList)



# todo
# 기존 bbsNo 보다 큰 게시물들 의 title 내용 키워드 검색
# 가장 높은 no 값을 저장
#

