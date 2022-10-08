word = input().lower()
word_list = list(set(word))
count = []
for i in word:
    cnt = word.count(i)
    count.append(cnt)

if count.count(max(count)) >= 2:
    print("?")
else:
    print(word_list[count.index(max(count))].upper())

# 문자열에 대한 접근이 필요하면 리스트 변환.
# 스트링에 대한 인덱스는 확인할 수 있는데 수정이 불가능
# set은 순서가 없어서 개별 인덱스 접근 자체 불가
# 튜플은 절대절대 수정 불가.
# 리스트 : O(N)
# 딕셔너리 쓰는 이유 : O(1)
# 파이썬 알고리즘 인터뷰 책에 나오는 링크드 리스트 같은 경우에는 잘 안나옴.
# 큐: 앞뒤로 추가 제거가능
# 링크드리스트: 삽입 삭제 용의
# range =  배열이다
# from collections import deque
# a = [1,2,3,4,5,6]
# a.pop() 연산 1번
# a.pop(0) 연산 6번

# a.popleft() 연산 1번
# a.append() 뒤엣것
# a.appendleft() 앞에 추가 연산 적게 하기위해 큐를 씀
