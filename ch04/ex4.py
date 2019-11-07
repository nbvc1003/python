

def average(*val):
    print('type :', type(val))
    if val == None or len(val) < 1:
        return None
    total = 0
    for i in val:
        total += i
    print('total :', total)
    print('len :' , len(val))
    return total/len(val)

print(average(12,11,33))
print(average())