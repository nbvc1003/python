

# 다른 패키지, 의 파일내용을 사용하고자 할때 import를 사용
import ch07.cal as c # as : 패키지명을 변경한다. 

# import를 사용할수 있는 패키지
# 3.3이전 의 결우 __init__.py 파일이 있어야 임포트 가능
# 3.3이후 디렉토리내 파일도 가능
#

print("다른곳에서 실행 :", c.plus(12,3))
print("다른곳에서 실행 :", c.minus(12,3))

