result = 0

try:
     [1, 2, 3][3]
     "a"+1
     4 / 0
except TypeError:
    result += 1 # int(0b0001)
except ZeroDivisionError:
    result += 2 # int(0b0010)
except IndexError:
    result += 4 # int(0b0100)
finally:
    result += 8 # int(0b1000)

# 순서대로 예외가 발생할때 예외처리 내용이 실행되고 try 내부 나머지 건너뛴다.
print(bin(result))

# print(int(0b10))