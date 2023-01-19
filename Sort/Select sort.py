A = [9,5,1,4,6,7,2,8,3,0]

for i in range(len(A)):
    min_index = i #가장 작은 원소의 인덱스
    for j in range(i+1,len(A)): #그 다음 인덱스부터 끝까지
        if A[min_index] > A[j]: #min index 보다 더 작은 값이 있다면
            min_index = j #그걸 min 인덱스로 정하고 스왑해준다.
    A[i],A[min_index] = A[min_index],A[i]
print(A)

