'''Problem : Buy and Sell Stock '''

#Code : 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices):
            buy = prices[0]
        else:
            return -1
        profit = 0
        for i in range(1, len(prices)):
            print(i)
            profit = max(profit, prices[i]-buy)
            buy = min(buy, prices[i])
        return profit
