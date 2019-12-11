from bs4 import BeautifulSoup
import urllib.request
# quote url의 한글 (utf8)이 포함되어 있을때 ASCII 형식으로 변경
from urllib.parse import quote

print('검색어를 입력하세요')
keyword = input()

# 1페이지당 기사 15개
page_num = int(input('페이지 갯수'))
output_file_name = input('저장할 파일명')
output_file = open(output_file_name, 'w',encoding='utf-8')
# check_new = 1뉴스
# more=1 더보기가 누른 상태..
# sorting = 3 정확도순 정렬, range= 3 전체 기간
for i in range(page_num):
    current_page_num = 1+ i*15
    # 쿼리문에 한글이 들어갈경우 quote 함수 사용..
    target_url = "http://news.donga.com/search?p="\
                 +str(current_page_num)+"&query="+quote(keyword)\
                +"&check_news=1&more=1&sorting=3&serch_date=1&range=3"
    source_code = urllib.request.urlopen(target_url)

    soup = BeautifulSoup(source_code, 'lxml', from_encoding='utf-8')
    # print(soup)
    for title in soup.find_all('p'): # p 테그나 class가 tit
        title_link = title.select('a')
        article_url = title_link[0]['href'] # 연결된 인터넷주소
        source_code_from = urllib.request.urlopen(article_url)
        # soup 첫번째 화면에서 연결된 뉴스
        soup = BeautifulSoup(source_code_from,'lxml',from_encoding='utf-8')
        #<div class=article_txt
        content_of_article = soup.select('div.article_txt')
        for item in content_of_article:
            string_item = str(item.find_all(text=True))
            output_file.write(string_item)

print(output_file_name, '에 저장완료')
output_file.close()







