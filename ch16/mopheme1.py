from konlpy.tag import *
from konlpy.corpus import kolaw

c = kolaw.open('constitution.txt').read()

hannanum = Hannanum();
kkma = Kkma()
komo = Komoran()
okt = Okt() # 가장 많이 쓰임..

print(hannanum.morphs(c[:40]))
print(kkma.morphs(c[:40]))
# 줄바꿈 제거 필요.
print(komo.morphs("\n".join([s for s in c[:40].split("\n") if s])))
print(okt.morphs(c[:40]))



