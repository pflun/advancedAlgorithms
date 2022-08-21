# -*- coding: utf-8 -*-
import decimal
class Solution(object):
    def minimumLines(self, stockPrices):
        if len(stockPrices) <= 1:
            return 0
        elif len(stockPrices) == 2:
            return 1

        res = 1
        rates = []
        stockPrices.sort()
        for i in range(len(stockPrices) - 1):
            # 分母为0
            if stockPrices[i][1] - stockPrices[i + 1][1] == 0:
                rates.append('#')
            else:
                curr_rate = decimal.Decimal(stockPrices[i][0] - stockPrices[i + 1][0]) / decimal.Decimal(stockPrices[i][1] - stockPrices[i + 1][1])
                rates.append(curr_rate)
        for i in range(len(rates) - 1):
            if rates[i] != rates[i + 1]:
                res += 1
        return res

test = Solution()
print test.minimumLines([[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]])
print test.minimumLines([[3,4],[1,2],[7,8],[2,3]])