

score = [78,99,45,88, 23, 66]
# max min, sum, avg  값구하는 함수

def score_max(numlist):
    result = 0
    for i in numlist:
        if result < i:
            result = i
    return result

def score_min(numlist):
    result = numlist[0]
    for i in numlist:
        if result > i:
            result = i
    return result

def score_sum(numlist):
    result = 0
    for i in numlist:
        result += i
    return result;

def score_avg(numlist):
    return score_sum(numlist)/len(numlist)

print(score_max(score))
print(score_min(score))
print(score_sum(score))
print(score_avg(score))
