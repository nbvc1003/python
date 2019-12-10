from konlpy.tag import *
from konlpy.corpus import kolaw

c = kolaw.open('constitution.txt').read()
print('원본 :' , c[:40])
print('--------------------------------------------------------')
hannaum = Hannanum()
kkma = Kkma()
komoran = Komoran()
okt = Okt() # 가장 많이 사용됨

print('한나눔', hannaum.nouns(c[:40]))
print('꼬꼬마', kkma.nouns(c[:40]))

# komoran 빈줄이 있으면 오류 발생
print('코모란', komoran.nouns("\n".join([s for s in c[:40].split("\n") if s ])))

print('OKT', okt.nouns(c[:40]))

