from bs4 import BeautifulSoup


# <ul> : 순서가 없는 리스트
# <li> : 리스트
# <a> : anchor
# href : 하이퍼링크
# tag 속에 있는 값들은 속성(attribute) 라고 한다.

# <> 시작태그, </> 끝태그
html = """
    <html>
        <body>
            <ul>
                <li><a href="http://www.naver.com">네이버</a></li>
                <li><a href="http://www.daum.net">다음</a></li>
                <li><a href="http://www.google.com">구글/a></li>
            </ul>
        </body>
    </html>
"""

soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all('a') # a테그를 전부 찾는다.

for a in links:
    print(a.attrs['href']) # a 의 'href' 속성값을 출력


