from konlpy.tag import Okt
from collections import Counter

noutn_count = 200
result_file_name = 'count.txt'

# donga1.py 에서 저장한 파일을 사용..
open_text_file = open('ab.txt', 'r', encoding='utf-8')
text = open_text_file.read()

okt = Okt()

nouns = okt.nouns(text) # 문장에서 명사만 추출한다.

# 명사와 갯수 쌍의 배열
count = Counter(nouns)

# print(count)
# 명사, 객수
tags = []
for n , c in count.most_common(200):
    temp = {'tag':n, 'count':c}
    tags.append(temp)

open_text_file.close()

open_result_file = open(result_file_name,'w',encoding='utf-8')
for tag in tags:
    noun = tag['tag']
    cnt = tag['count']
    open_result_file.write('{} {}\n'.format(noun, cnt))
open_result_file.close()
print(result_file_name, '에 저장 완료')
    