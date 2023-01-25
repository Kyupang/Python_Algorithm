import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
a= list(map(int,input().split()))
a2 = sorted(list(set(a)))
b=[]

#시간복잡도 n은 백만*백만= 1000000000000 1조
#파이썬은 1초에 2천만 시간제한 2초니까 4천만 끝
#but dic으로 하면 O(1)
for i in range(len(a)):
    count = 0
    for j in range(len(a2)):
        if a[i] > a2[j] :
            count+=1
        else:
            continue
    b.append(count)

for i in range(len(b)):
    print(b[i],end =" ")