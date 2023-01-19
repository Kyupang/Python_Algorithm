A = [9,5,1,4,6,7,2,8,3,0]
#움직이는 인덱스와 움직이지 않는 인덱스를 구분해서 사용
def quick_sort(array,start,end):
    if start>= end: #어레이의 원소가 하나라면
        return
    pivot =start
    left = start+1
    right = end
    while(left<= right):
        #피벗보다 큰 데이터를 찾을 때까지 반복
        while(left<=end and array[left]<=array[pivot]):
            left+=1
        #피벗보다 작은 데이터를 찾을 때까지 반복
        while(right>start and array[right]>=array[pivot]):
            right-=1
        #엇갈렸다면 작은데이터와 피벗을 교체
        if(left>right):
            array[right],array[pivot] =array[pivot],array[right]
        #엇갈리지 않았다면 큰 데이터와 작은 데이터를 교체
        else:
            array[left],array[right]= array[right],array[left]

    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

quick_sort(A,0,len(A)-1)
print(A)

# 파이썬의 장점으로 짧게 구현할 수 있다.
array = [5,7,9,0,3,1,6,2,4,8]
def quick_sort_py(array):
    if len(array)<=1:
        return array
    pivot = array[0]
    tail =array[1:]

    left_side = [x for x in tail if x<=pivot]
    right_side = [x for x in tail if x> pivot]

    return quick_sort_py(left_side) + [pivot] + quick_sort_py(right_side)

print(quick_sort_py(array))