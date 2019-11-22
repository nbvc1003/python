

l1 = ['허걱','허각','허공']
l2 = ['\n구렁이','\n팔랑이','\n팔렁이']
l3 = ['\n구렁이','\n구렁삼','\n구렁사']

file = open("test2.txt",'w',encoding='utf-8')

file.write('금요일\n');file.write('오후\n');file.write('4시40분\n')
file.write('\n'.join(l1))
file.writelines(l2)
file.write(''.join(l3))

file.close()