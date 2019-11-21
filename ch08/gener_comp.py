# Generator Expression

# 내부 적으로는 yeild 를 수행
g1 = (n*n for n in range(21))

# 리스트로 현변환하고 전부 출력
# print(list(g1))

for i in range(11):
    # 내부적으로 yeild 가 불리면서 순차적으로 처리 된다.
    val = next(g1)
    print(val)

# 나머지 전부 출력
# yeild로 멈춰 있던 이후 부분이 출력된다.
print("---------------------------------------")
for i in g1:
    print(i)