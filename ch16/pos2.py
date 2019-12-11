from konlpy.tag import *
from konlpy.corpus import kolaw

c = kolaw.open('constitution.txt').read()

hannanum = Hannanum()
kkm = Kkma()
komo = Komoran()
okt = Okt()

# 품사 tag 부착
print(hannanum.pos(c[:40]))
print(kkm.pos(c[:40]))
# \n\n 와같은 라인의 \n 하나를 삭제 하는 역활 : \n\n -> \n
print(komo.pos("\n".join([s for s in c[:40].split("\n") if s ])))
print(okt.pos(c[:40]))

# 품사 tag의 설명
print(hannanum.tagset)
print(kkm.tagset)
print(okt.tagset)

