from bs4 import BeautifulSoup # XML, HTML
import urllib.request as req
import requests
import time


__url = "http://www.inven.co.kr/board/destinyguardians/5294" #파티찾기
# __url = "http://www.inven.co.kr/board/destinyguardians/5051" #전체 게시판

__bbsList = []
__bbsNo = 0

def telegram_bot_sendtext(bot_message):
    bot_token = '327497093:AAGJCRubUJv36_rwbD2Ul4D_DkXoA-ZORag'
    bot_chatID = '51404588'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

def HtmlPase(url):

    res = req.urlopen(url)
    soup = BeautifulSoup(res, 'html.parser')

    bbs = soup.select_one("div#powerbbsBody")
    bbsNo = 0
    listItems = bbs.select("tr.ls")

    for item in listItems:
        itemNo = str(item.select_one(".bbsNo").string).strip()
        itemDate = str(item.select_one(".date").string).strip()
        itemSub = str(item.select_one(".bbsSubject > a.sj_ln").string).strip()
        itemHref = item.select_one(".bbsSubject > a").attrs['href']
        # print(itemHref)
        # 게시판리스트의 No값이 숫자인 게시물만 dic으로
        bbsListDic = {}
        if itemNo.isdigit() and itemDate.find(':'):
            # print(itemNo, itemSub)
            bbsListDic['id'] = int(itemNo)
            bbsListDic['date'] = itemDate
            bbsListDic['subject'] = itemSub
            bbsListDic['a_href'] = itemHref
            __bbsList.append(bbsListDic)
            bbsNo
            if bbsNo < int(itemNo):
                bbsNo = int(itemNo)

    print(len(listItems))
    return bbsNo

def KeywordSearch(keyword):
    print(keyword, len(__bbsList))
    findList = []
    for item in __bbsList:
        if item['subject'].find(keyword) > 0:
            findList.append(item)
        if len(findList) > 5 :
            break;


    if len(findList) > 0:
        for msg in findList:
            # 게시판 링크만 전달
            print(msg['subject'])
            print(msg['a_href'])
            telegram_bot_sendtext(msg['a_href'])
    else:
        print("검색결과가 없습니다.")




keyword = input('검색 키워드 :')

while True:
    __bbsList.clear()
    bbsNo = HtmlPase(__url)

    if bbsNo > __bbsNo or __bbsNo == 0:
        KeywordSearch(keyword)
    else:
        print("신규 게시글이 없습니다. keyword :" ,keyword)

    __bbsNo = bbsNo

    print("마지막 게시물 번호 :", __bbsNo)
    time.sleep(5)





