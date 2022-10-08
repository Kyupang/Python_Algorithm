c = int(input())

for i in range(c):
    Num = list(map(int,input().split()))
    avg = sum(Num[1:]) / Num[0]
    over = 0
    for j in Num[1:]:
        if j > avg:
            over +=1
    rate = (over / Num[0]) *100
    print("{:.3f}%".format(rate))


