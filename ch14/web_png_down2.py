import urllib.request

url = "http://uta.pw/shodou/img/28/214.png"
savename = "test2.png"

url2 = "https://imgnews.pstatic.net/image/025/2019/12/05/0002958166_001_20191205140701078.jpg?type=w647"

# 특정경로에 저장
savename2 = "E:/nbvc/python/kang.jpg"


# mem = urllib.request.urlopen(url).read()
# with open(savename, mode='wb') as f:
#     f.write(mem)
# print('저장완료')

mem = urllib.request.urlopen(url2).read()
with open(savename2, mode='wb') as f:
    f.write(mem)

print('저장완료2')
