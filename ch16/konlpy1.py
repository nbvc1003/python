from konlpy.corpus import kolaw, kobill
print(kolaw.fileids(), kobill.fileids())

# 헌법 전문
c = kolaw.open('constitution.txt').read()
print(c[:40])

print('--------------------------------------------------------')
# 국회 속기록
k = kobill.open('1809899.txt').read()
print(k[:300])

