
gender = input("남/영 중 입력하세요")

cnt = int(input("팔굽혀펴기 회수를 입력하세요 "))

if gender == '남':
    if cnt >= 10 :
        grade = "합격"
    else :
        grade ="불합격"
else :
    if cnt >= 5:
        grade = "합격"
    else:
        grade = "불합격"

print(grade)
            

