
# def 함수 선언
def strlen(st):
    return len(st) # st의 길이를 리턴


data = ['Morning','Afternoon','evening','Night']

#함수를 실행한 결과를 가져와서 그것을 기준으로 sort
# key = lower, upper 대소문자로 바꾼후 정렬
# key = 요소별 숫자 값을 줄경우 숫자의 내림차순으로
data.sort(key=strlen)
print(data)

data.sort(key=strlen, reverse=True)
print(data)