from urllib.parse import urljoin # 상대경로를 절대경로 로 변경

# url: 전체 주소  uri : html/a.html -> 폴더위치 + html
base = "http://example.com/html/a.html"

print(urljoin(base, "b.html")) # 절대경로로 변경

print(urljoin(base, "sub/c.html")) # 하위 폴더 만들고 추가
print(urljoin(base, "../index.html")) # 상위폴더로 이동한다음 추가

print(urljoin(base, "../img/hoge.png"))
print(urljoin(base, "../hoge.css"))

# / :  http://ip(주소(도메인)):포트번호 를 시작으로 절대경로
print(urljoin(base, "/huge.html")) # -> http://example.com/huge.html

# http:// or // 와 같이 시작 할 경우 절대경로로된 주소이니 변경하지 말라는 의미
print(urljoin(base, "http://www.daum.net/index.html"))
print(urljoin(base, "//www.naver.com/index.html")) # http:// == //

