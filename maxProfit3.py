# -*- coding: utf-8 -*-
# 最关键的地方是要明白at most two trasaction 怎么用
# II允许两次买卖，但同一时间只允许持有一支股票。也就意味着这两次买卖在时间跨度上不能有重叠（当然第一次的卖出时间和第二次的买入时间可以是同一天）。既然不能有重叠可以将整个序列以任意坐标i为分割点，分割成两部分：
# prices[0:n-1] => prices[0:i] + prices[i:n-1]
# 对于这个特定分割来说，最大收益为两段的最大收益之和。每一段的最大收益当然可以用I的解法来做。而III的解一定是对所有0<=i<=n-1的分割的最大收益中取一个最大值。为了增加计算效率，考虑采用dp来做bookkeeping。目标是对每个坐标i：
# 1. 计算A[0:i]的收益最大值：用minPrice记录i左边的最低价格，用maxLeftProfit记录左侧最大收益
# 2. 计算A[i:n-1]的收益最大值：用maxPrices记录i右边的最高价格，用maxRightProfit记录右侧最大收益。
# 3. 最后这两个收益之和便是以i为分割的最大收益。将序列从左向右扫一遍可以获取1，从右向左扫一遍可以获取2。相加后取最大值即为答案。

class Solution(object):
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0

        res = 0
        currmin1 = float('inf')
        res1 = 0

        for price in prices:
            if price < currmin1:
                currmin1 = price
            if price - currmin1 > 0:
                res1 = max(res1, price - currmin1)

        for i in range(len(prices)):
            prices1 = prices[:i]
            prices2 = prices[i:]

            currmin1 = float('inf')
            res1 = 0

            for price in prices1:
                if price < currmin1:
                    currmin1 = price
                if price - currmin1 > 0:
                    res1 = max(res1, price - currmin1)

            currmin2 = float('inf')
            res2 = 0

            for price in prices2:
                if price < currmin2:
                    currmin2 = price
                if price - currmin2 > 0:
                    res2 = max(res2, price - currmin2)

            res = max(res, res1 + res2)

        return res

test = Solution()
print test.maxProfit([7, 2, 9, 1, 7, 10])