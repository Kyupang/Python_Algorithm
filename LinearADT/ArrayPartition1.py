class solution:
    def arrayPairSum(self,nums:list[int])-> int:
        sum=0
        nums.sort()
        pair = []

        for n in nums:
            pair.append(n)
            if (len(pair)==2):
                sum +=min(pair)
                pair = []
        return sum

    def arrayPairSum2(self,nums:list[int])->int:
        return sum(sorted(nums)[::2])


sol = solution()
nums = [1,4,2,3]
print(sol.arrayPairSum(nums))
print(sol.arrayPairSum2(nums))

