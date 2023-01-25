import sys
def input():
    return sys.stdin.readline().rstrip()

S = str(input())
result = int(S[0])
for i in range(len(S)):
    num = int(S[i])
    if num<=1 or result <=1:
        result += num
    else:
        result *= num
print(result)

