
# with ~ as 를 사용하면 자동으로 close
with  open ('capital.txt','r',encoding='utf-8') as f:
    for line in f:
        data = line.strip().split(':')
        print('%s의 수도는 ? '%(data[0]))
        capital = input()
        if capital == 'q': break
        if capital == data[1]:
            print('good!')
        else:
            print('놀구 있네 %s 에요 '%(data[1]))

print('프로그램 종료')

