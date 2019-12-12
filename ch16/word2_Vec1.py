import codecs
from typing import Optional, List

from gensim.models import word2vec
from bs4 import BeautifulSoup

from konlpy.tag import Okt

# BEXX0003.txt 는 utf -16
fp = codecs.open('BEXX0003.txt','r',encoding='utf-16')
soup = BeautifulSoup(fp, 'html.parser')
body: Optional[BeautifulSoup] = soup.select_one('body > text')
text: object = body.getText()
okt = Okt()
results: List[str] = []
# print(text)
print("----------------------------------------------------------------")
lines = text.split("\r\n") # "\r\n" (앤터) 줄바꿈을 기준으로 분리해서 list() 형태로

for line in lines:
    # 형태소분석 
    r = []
    # print(line)
    malist = okt.pos(line, norm=True, stem=True) # 
    # word[0]: 단어, word[1]: 품사명
    for word in malist:
        # 품사가 조사, 어미, 구둣점은 제외
        if not word[1] in ["Josa","Eomi","Punctuation"]:
            r.append(word[0])
    r1 = " ".join(r).strip() # \n, \t 제거
    results.append(r1)
    # print(r1)
#파일로 출력

imsi_file = 'toji.wakati' # 임시파일

with open(imsi_file, 'w',encoding='utf-8') as f:
    f.write('\n'.join(results)) # 아이템별 \n을 넣어서 넣는다.
# word2vec 모델 만들기
data = word2vec.LineSentence(imsi_file)
# 200차원, 앞뒤로 10개 단어,  min_count=2 :2번이상 언급, sg : Skip_gram
model = word2vec.Word2Vec(data, size=200, window=10, hs=1, min_count=2, sg=1)

model.save('toji.model')
print('모델 생성 완료')

        
    

