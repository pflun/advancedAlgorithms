# find all ascending region
class Solution(object):
    def maxProfit(self, prices):
        maxprofit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                maxprofit += prices[i] - prices[i - 1]
        return maxprofit





test = Solution()
print test.maxProfit([7, 2, 9, 1, 7, 4])