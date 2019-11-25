import os
import shutil
# ./ 현재 디렉토리 파일 내용 리스트 출력
curlist = os.listdir("./")
for name in curlist:
    print(name)

# 현재 디렉토리의 정보를 출력
print(os.stat('./'))

# 디렉토리 생성
os.mkdir('imsi')

# # # 안에 데이터가 있으면 삭제안됨
# os.rmdir('imsi')

#  파일 삭제시 os.remove()
# 디렉토리내의 파일 유무와 상관없이 삭제
# shutli 라이브러리의 shutil.rmtree() 를 사용한다.


