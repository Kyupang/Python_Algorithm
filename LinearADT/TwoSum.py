class solution :
    #비효율적인 풀이법 시간복잡도 O(n^2)
    def twoSum(self, nums: list[int], target : int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

    #이 풀이도 마찬가지로 O(n^2)이지만 실행속도가 훨씬 빠르다
    #in 의 복잡도가 O(n)이기 때문에 in이 중첩해서 있어서 그렇다.
    def twoSum2(self,nums:list[int],target : int)-> list[int]:
        for i, n in enumerate(nums):
            complement = target -n

            if complement in nums[i+1 : ]:
                #i+1을 해주는 이유는 i번째 인덱스 다음 것들부터 검사를 하기 때문에
                #원래 인덱스는 i+1이 후의 인덱스이다.
                #예를들어 i+1을 안하게 되면 이 루프는 [value 7:]의 배열을 0부터 인덱싱한다.
                #근데 배열안에 7은 원래 1번 인덱스에 있었으니 2의 인덱스를 리턴하려면 i+1을 더해주어야한다.
                return [nums.index(n), nums[i+1:].index(complement) + (i+1)]

    #나는 이 알고리즘이 이해하기도 쉽고 풀 수 있을 것 같아 3번을 채택하였다.
    def twoSum3(self, nums:list[int], target:int)->list[int]:
        nums_map = {}
        #키와 값을 바꿔서 딕셔너리로 저장 //nums_map = {2:0,7:1,11:2,15:3}
        #nums_map[key] = value
        for i, num in enumerate(nums):
            nums_map[num] = i
        #타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            # key in dic and i = 0,1,2,3 != nums_map[key]의 value인 0,1,2,3과 달라야한다.
            if target - num in nums_map and i != nums_map[target-num]:
                return [i, nums_map[target - num]]

    def twoSum4(self,nums:list[int],target:int)->list[int]:
        nums_map = {}
        for i,num in enumerate(nums):

            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] =i

    #값을 찾아내는 문제였다면 이렇게 풀어도 상관없지만
    #정렬되어 있는 리스트가 아니기 때문에 이렇게 풀 수 없다.
    #정렬을 넣어도 인덱스가 망가지니 틀린 풀이이다.
    def twoSum5(self,nums:list[int],target:int)->list[int]:
        nums.sort()
        left,right = 0, len(nums)-1
        while not left == right:
            #합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
            if nums[left]+nums[right] < target:
                left+=1
            #합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
            elif nums[left] + nums[right] > target:
                right-=1
            else:
                return [left,right]


sol = solution()
target = 9
nums = [11,7,2,15]



print(sol.twoSum(nums,target))
print(sol.twoSum2(nums,target))
print(sol.twoSum3(nums,target))
print(sol.twoSum4(nums,target))
print(sol.twoSum5(nums,target))

