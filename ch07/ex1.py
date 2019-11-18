

mypi = 3.14

# 원의 면적  r * r * 3.14

def area(r):
    return r**2*mypi

# 자체적으로 실행 
# 외부에서 실행시 실행에서 제외
print("name = ", __name__)
if __name__ == "__main__":
    print(__name__)
    print(area(5))