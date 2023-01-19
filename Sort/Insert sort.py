A = [9,5,1,4,6,7,2,8,3,0]

for i in range(1,len(A)):
    for j in range(i,0,-1): # 인덱스 i 부터 1까지 (0이 1이니까) 1씩 감소하며 반복
        if A[j] < A[j-1]: #한 칸씩 왼쪽으로 이동
            A[j],A[j-1] =  A[j-1],A[j]
        else:
            break
print(A)