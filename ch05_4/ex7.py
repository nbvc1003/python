

# 1: 1000
def kor_to_usd(won):
    result = []
    for i in won:
        result.append(i/1000)
    return result

# 1 : 0.08,  8/1000 *1000 = 8
# 1000 : 8    1000/8 : 1
def usd_to_jpy(dollars):
    result = []
    for i in dollars:
        result.append(i * 1000/8)
    return result


amounts = [1000, 2000, 3000, 5000, 8000, 13000, 21000, 34000]
print("한국 화폐" + str(amounts))

# 한국 화폐

#미국 화폐
print("미국 화폐" , kor_to_usd(amounts))
print("일본 화폐" , usd_to_jpy(kor_to_usd(amounts)))