
kor = 80
eng = 75
math = 55
print((kor+eng+math)/3)
score = {'kor':80, 'eng':75, 'math':55}
sum = 0
for sc in score.values():
    sum += sc
print('평균 :', sum/len(score.values()))

