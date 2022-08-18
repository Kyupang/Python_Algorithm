#2포인터를 이용하는 방법
def reverseString(s: list[str]) :
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left +=1
        right -=1
    return s

a = ["h","e","l","l","o"]
print(reverseString(a))


#파이썬 스타일
def reverseString2(s:list[str]):
    s[:] =s[::-1]
    return s

print(reverseString2(a))