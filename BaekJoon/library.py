result = eval("(3*5)%2")
print(result)
print()
#순열과 조합
#순서를 고려하면 순열
#순서를 고려하지 않으면 조합
from itertools import *
data = ['A','B','C']
result2 =list(permutations(data,3))
print(result2)
result3 =list(combinations(data,2))
print(result3)
#중복 순열 중복 조합
#중복을 포함하는데 순서를 고려하느냐 마느냐
#중복순열 순서를 고려함
result4 = list(product(data,repeat=2))
print(result4)
#중복조합 순서를 고려하지 않음
result5 = list(combinations_with_replacement(data,2))
print(result5)

#collection Counter 라이브러리
from collections import Counter
print()
counter = Counter([1,2,3,4,5,5])
print(counter[5]) #5가 몇 번 나왔냐
print(dict(counter)) #이거 딕셔너리로 정렬해라

S=[1,51,5,1,5,61]
cnt = Counter(S).most_common() #배열에서 가장많이 등장한애
mode = []

for i in cnt:
    if cnt[0][1] ==i[1]: #튜플의 2번째 요소가 cnt의 두번째 요소와 같으면
        mode.append(i[0])
    else:
        break
if len(mode) == 1: #최빈값을 꺼내놔
    print(mode[0])
else:
    mode.sort()
    print(mode[1])

#math 라이브러리
#최대공약수,최소 공배수
import math
def lcm(a,b):
    return a*b//math.gcd(a,b)
a=21
b=14

print()
print(math.gcd(21,14)) #같이 나누어 떨어지는 수에서 가장 큰값 최대 공약수
print(lcm(a,b)) #최소 공배수
