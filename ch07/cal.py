

def plus(x,y):
    return x + y
def minus(x,y):
    return x - y

def multiply(x,y):
    return x * y
def divide(x,y):
    return x/y


# 외부에서 실행할경우 실행하지 않는다.
# import와 같이 다른 파트에서 가져와서 실행할경우 아래내용을 실행하지 않는다.
if __name__ == "__main__":
    print(plus(12,3))
    print(minus(12,3))
    print(multiply(12,3))
    print(divide(12,3))

