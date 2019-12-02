import re # 정규식을 시원하는 패키지


# 주민번호 뒷자리를 별표로 변경

data = """
park 800905-1049118
kim 700905-1059119
"""

# re_pattern_basic1.py 에 비해 상당히 간단해짐..
# 정규식 패턴정의
pat = re.compile("(\d{6})-\d{7}") # 숫자6자리 - 숫자 7자리
print(pat.sub("\g<1>-*******", data)) # sub : 치환하는 함수

# \d{3}-\d{3,4}-\d{4} -> 전화번호 채크 (숫자3자리, 숫자 3or 4자리, 숫자 4자리

