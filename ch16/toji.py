import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Okt

# utf-16 으로 인코딩된 파일을 열고 글자를 가져 온다.
fp = codecs.open('BEXX0003.txt','r', encoding='UTF-16')
soup = BeautifulSoup(fp, 'html.parser')

# body > text 하위내용만
body = soup.select_one("body > text")
text = body.getText() # text 읽어 온다.

okt = Okt()
word_dic = {}

# 문서를 줄단위로 잘라서 배열로 만든다.  
lines = text.split("\r\n") # \r\n : Enter
for line in lines:
    malist = okt.pos(line) # (단어와 , 품사) 형식으로 만들어 준다.
    for word in malist:
        if word[1] == 'Noun': # 품사가 명사이면..
            if not (word[0] in word_dic): # word_dic 에 word[0]의 키값이 없으면 만들어라..
                word_dic[word[0]] = 0
            word_dic[word[0]] += 1 # 같은 단어를 발견 할때 마다 카운트 증가

# . items() 키와 값  (key, values) == items

keys = sorted(word_dic.items(), key = lambda x:x[1], reverse=True) # list[x1[2], x2[2],....]  : x[1] 값이 큰순서로 정렬

# reverse=True 오름차순으로
for word, count in keys[:50]:
    print("{}({})".format(word,count),end='')