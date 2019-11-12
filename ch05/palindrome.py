



# 문자열 거꾸로 쓰기
def is_palindrome(word):
    #원본의 변경시키지 않는다. 
    return word == word[::-1]

def is_palindrome2(word):
    result = ''
    for i in range(len(word)-1, -1,-1):
        result += (word[i])
    return word == result


print(is_palindrome("racecar"))
print(is_palindrome2("rececar1"))

print(is_palindrome("rececer1111"))

print(is_palindrome("토마토"))
print(is_palindrome2("토마토"))