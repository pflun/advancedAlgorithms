class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > profit:
                    profit = prices[j] - prices[i]
        return profit

    def maxProfit2(self, prices):
        minprice = float("inf")
        maxprofit = 0
        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            elif prices[i] - minprice > maxprofit:
                maxprofit = prices[i] - minprice
        return maxprofit

    def maxProfit3(self, prices):
        # DP: f[i] = max profit if sell at i day
        if len(prices) <= 1:
            return 0

        res = 0
        minprice = min(prices[0], prices[1])
        maxprofit = [0] * len(prices)
        maxprofit[1] = prices[1] - prices[0]

        for i in range(2, len(prices)):
            minprice = min(minprice, prices[i - 1])
            if maxprofit[i - 1] < 0:
                # if prev max profit is negative, abandon prev and start over from today
                maxprofit[i] = prices[i] - minprice
            else:
                # today's max = yesterday's max + today's profit
                maxprofit[i] = maxprofit[i - 1] + prices[i] - prices[i - 1]

        for j in maxprofit:
            res = max(res, j)

        return res


test = Solution()
print test.maxProfit2([7, 1, 5, 3, 6, 4])