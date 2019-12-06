import requests
import json
# API 키를 지정합니다. 자신의 키로 변경해서 사용해주세요.
apikey = "474d59dd890c4108f62f192e0c6fce01"
# 날씨를 확인할 도시 지정하기
cities = ["Seoul,KR", "Tokyo,JP", "New York,US"]
# API 지정
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"
# 켈빈 온도를 섭씨 온도로 변환하는 함수
k2c = lambda k: k - 273.15
# 각 도시의 정보 추출하기 -
for name in cities:
    # API의 URL 구성하기
    url = api.format(city=name, key=apikey)
    # API에 요청을 보내 데이터 추출하기
    r = requests.get(url)
    data = json.loads(r.text)
    print("+도시=",data["name"])
    print("|날씨=", data["weather"][0]["description"])
    print("|최저 기온 =",round(k2c(data["main"]["temp_min"]),2))
    print("|최고 기온 =", round(k2c(data["main"]["temp_max"]),2))
    print("|습도 =", round(k2c(data["main"]["humidity"]),2))
    print("|기압 =", round(k2c(data["main"]["pressure"]),2))
    print("|풍향 =", round(k2c(data["wind"]["deg"]),2))
    print("|풍속 =", round(k2c(data["wind"]["speed"]),2))
    print("\n")
    


