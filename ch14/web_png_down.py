import urllib.request

url = "http://uta.pw/shodou/img/28/214.png"
savename = 'test.png'


urllib.request.urlretrieve(url, savename)
#경로가 없을경우에는 현재 위치에 저장

url = "https://imgnews.pstatic.net/image/025/2019/12/05/0002958166_001_20191205140701078.jpg?type=w647"
urllib.request.urlretrieve(url, "webTest.jpg")


