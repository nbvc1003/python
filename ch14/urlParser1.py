from urllib.parse import urlparse

result = urlparse("https://docs.python.org/3.5/library/ ")

# scheme='https' : 프로토콜
# netloc='docs.python.org  : 네트워크 위치 , ip주소(도메인)
# params 매게변수
# query : &로 구분되는 값
# fragment : 문서내의 앵커등 지정.

print(result)
