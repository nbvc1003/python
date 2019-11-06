

print("정수를 입력하세요")
num1 = input() # 입력받은 값은 문자열로 받는다. 
print("정수를 입력하세요")
num2 = input()

print(num1 + num2) # 문자열로 출력
print(int(num1) + int(num2)) # 숫자형식으로 바꿔서

print("{} + {} = {}".format(num1, num2, num1+num2))
print("{} + {} = {}".format(num1, num2, int(num1)+int(num2)))