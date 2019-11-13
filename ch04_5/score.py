
# 국어, 영어, 수학, 점수를 입력 받아서
# score함수를 만들어서 총점 , 평균을 출력
# 평균을 소수점 2자리 까지 출력

kor = int(input('국어점수 :'))
eng = int(input('영어점수 :'))
math = int(input('수학점수 :'))

def score (kor, eng, math):
    total = kor+eng+math
    print(total)
    print("평균 :", round(total/3, 2))
    print("평균 : %0.2f"%(total / 3))

score(kor, eng, math)