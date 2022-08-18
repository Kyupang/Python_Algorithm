t = int(input())
result = ''
for i in range(t):
    n,letter = input().split()
    for j in range(len(letter)):
        print(letter[j] * int(n),end="")
    print()
