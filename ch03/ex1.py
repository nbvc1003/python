

print("값 입력 ? :")
n = int(input()) # 외부에서 입력 받은 값
a = [1,1] #초기 배열 선언

for b in range(2, n):
    a.append(a[b-2] + a[b-1])

print ('n번째 값 = ' , a[n-1])

#
def fibo(n):
    if(n<2):
        return 1
    else :
        return fibo(n-2) + fibo(n-1)

print('fibo(7) =', fibo(7))