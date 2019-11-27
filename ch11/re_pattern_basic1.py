

# 주민번호 뒷자리를 별표로 변경

data = """
park 800905-1049118
kim 700905-1059119
"""

result = []
for line in data.split("\n"): # data를 2개로 분리 줄바꿈 기준으로 분리
    print(line)
    word_result = []

    for word in line.split(" "): # 공백 기준으로 분리
        # print(word)
        # 길이가 14자, 뒤쪽 6자리가 숫자 이면 주민번호로 판단.
        if len(word) == 14 and word[:6].isdigit():
            word = word[:6] + "-"+"*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))
            
    
