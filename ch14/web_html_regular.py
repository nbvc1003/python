from bs4 import BeautifulSoup
import re

html = """
    <ul>
        <li><a href="hoge.html">hoge</a></li>
        <li><a href="https://example.com/fuga">fuga*</a></li>
        <li><a href="https://example.com/foo">foo*</a></li>
        <li><a href="http://example.com/aaa">aaa</a></li>
    </ul>
"""

soup = BeautifulSoup(html, 'html.parser')
# ^ 시작, $ 끝, * 포함
# 11장 정규식 내용. 참고 
list = soup.find_all(href=re.compile(r'^https://'))
# 요소중에서 href 데이터 내용이 정규식 조건으로 정의한 내용과 일치하는 요소 검색

for i in list:
    print(i.attrs['href'])