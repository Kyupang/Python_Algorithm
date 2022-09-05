import sys

class solution:
    def maxProfit(self,prices:list[int])->int:
        profit = 0
        min_price = sys.maxsize
        #price번 쨰에 있는 요소이다.
        for price in range(0,len(prices)):
            min_price = min(min_price,price)
            profit = max(profit, price - min_price)
        return profit

prices = [7,1,5,3,6,4]
sol = solution()
print(sol.maxProfit(prices))