import urllib.request

url = "http://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url)
data = res.read()
print(type(data))
# byte 데이터 -> text
text = data.decode("utf-8")
print(text)



