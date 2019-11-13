

eng = ['home','desk','note','moning','age']
kor = ['집','책상','공책', '아침','나이']

# dic생성 : key를 eng, value를 kor로 생성
# 영어로 질문하고 한글로 답을 받아서
# 맞으면 정답 틀리면 오답 답은 XX 입니다. 출력

d1 = dict(zip(eng,kor))

for i in d1:
    temp = input('{} ? '.format(i))
    if temp == d1[i] :
        print('정답 입니다. ', d1[i])
    else:
        print('오답입니다. 답은 {} 입니다. '.format(d1[i]))
        







