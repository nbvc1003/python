

PI = 3.14 
# 변수명을 대문자로 사용할경우 값을 변경하지않는 상수로 간주한다.  
def area(r):
    return r *r * PI

r = 10
print('반지름이 {}인 원의 면적 {}'.format(r, area(r)))
r = 5
print('반지름이 {}인 원의 면적 {}'.format(r, area(r)))