

def var(*argv): # 갯수가 고정되지 않은 여러개 값
    for s in argv:
        print(s)


var('안녕하세요', "반갑습니다.", "누구세요")
var("대박","사건", "이건뭐야","김건모야")


def var1(*argv, a):
    for s in argv:
        print(s)

# 가변변수 뒤에 또 다른 변수 가 있을경우 사용시 특정해줘야 한다.
var1('안녕하세요', "반갑습니다.", a = "누구세요")