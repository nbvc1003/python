import re

s = '<html><head><title>대박</title>'

print(len(s))
# <.*> 욕심껏 최대 가능한 것을 참조 greed
print(re.match('<.*>',s).span()) # span은 (시작인덱스, 끝인덱스)
print(re.match('<.*>',s).group())


# <.*?> 욕심을 제한하여  최대 가능한 것을 참조 non-greed
# 결과적으로 첫번째 태그만 가져온다
print(re.match('<.*?>',s).span()) # span은 (시작인덱스, 끝인덱스)
print(re.match('<.*?>',s).group())