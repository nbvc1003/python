
#  하나의 문자열을 입력 받고 입력 받은 문자열을 while을 이용해서 뒤집어서
# # 출력해보기
# #  하나의 문자열을 입력 받고 입력 받은 문자열을 for를 이용해서 뒤집어서 출력해보기
# #  다음의 경로명에서 경로명과 파일명을 분리
# # s = ‘usr/local/bin/python’
# # dic = ‘/usr/local/bin’
# # filename = ‘python’

s = 'usr/local/bin/python'
dic = '/usr/loacl/bin'
filename = 'python'

sp = s.split("/")
l = len(sp)

print(sp[::-1])

result= []
while(l>0 ):
    l = l - 1
    print(sp[l],end=" ")

print('\n')

a = len(sp)
for i in range(a-1,-1,-1):
    print(sp[i])


# a = len(result)
#
# for i in range( 0, len(result)-1):
#     print(result[i])






