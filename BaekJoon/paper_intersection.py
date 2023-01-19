import sys

def input():
    return sys.stdin.readline().rstrip()
N = int(input())
paper = [[0]*100 for i in range(100)]

for _ in range(N):
    a,b = map(int,input().split())
    for i in range(10):
        for j in range(10):
            paper[a+i][b+j] =1

ans = 0
for i in paper:
    ans += sum(i)
print(ans)




