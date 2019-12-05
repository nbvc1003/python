from bs4 import BeautifulSoup

html = """
    <html>
        <body>
            <h1>좋아하는 과일</h1>
            <ul>
            <li price="200">산딸기</li>
            <li price="100">집딸기</li>
            <li price="50">판딸기</li>
            <li price="120">죽딸기</li>
            <li price="10">알딸기</li>
            <li price="150">뱀딸기</li>
            </ul>
        </body>
    </html>
"""

# 제목과, 과일명 출력

soup = BeautifulSoup(html,'html.parser')

print(soup.html.body.h1.string)

lists = soup.find_all('li')

for l in lists:
    print("가격 : {}, 이름 :{}".format(l.attrs['price'], l.string))



