

file = open("test.txt", 'w', encoding='utf-8')
# w : 기존파일에 덮어쓰기 a : 기존파일에 이어쓰기 x : 기존파일 없을때만

file.write('Hello python \n')
file.write('안녕 컴동지들 \n')

lines = ['안녕하세요', '누구세요','반갑습니다.']
lines2 = ['대박\n', '사건\n','허걱\n']
lines0 = ['줄단위로\n','경우\n','줄단위로쓰기\n']
# '\n'.join(strs)  strs 각 원소에 결합시켜준다.
file.write('\n'.join(lines))
file.write(''.join(lines2))

# list 형식을 한번에 입력할때
file.writelines(lines0)



file.close()
