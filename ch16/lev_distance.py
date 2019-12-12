def cal_distance(a,b):
    if a == b: return 0
    a_len = len(a)
    b_len = len(b)
    # 한쪽 단어가 없을때 다른쪽 단어의 길이 값으로 리턴  
    if a == '': return b_len
    if b == '': return a_len

    # 2차원 표 (a_len+1, b_len+1
    matrix = [[] for i in range(a_len+1)]
    for i in range(a_len + 1):
        # 리스트 안에 모두 사이즈 b_len+1 의 0으로 채워진 리스트를 입력
        matrix[i] = [0 for j in range(b_len+1)]
    # 2차원 배열일때 열과 행에 해당하는 값들을 0,1,2,3,4,5 형식으로 채워준다.
    for i in range(a_len+1):
        matrix[i][0] = i
    for j in range(b_len +1):
        matrix[0][j] = j

    for i in range(1,a_len+1):
        ac = a[i-1]
        for j in range(1,b_len+1):
            bc = b[j-1]
            cost = 0 if (ac == bc) else 1
            matrix[i][j] = min([
                matrix[i-1][j] + 1, # 문자삽입
                matrix[i][j-1] + 1, #문자 제거
                matrix[i-1][j-1] + cost # 분자 편집
            ])
    return matrix[a_len][b_len]

# 가나다라 와 가마바라 의 거리
print(cal_distance("가나다라","가마바라"))
samples =  ["신촌역","신천군","신천역","신발","마곡역"]
base = samples[0]
r = sorted(samples, key=lambda n : cal_distance(base, n))
for n in r:
    print(cal_distance(base, n), n)