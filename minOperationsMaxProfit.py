class Solution(object):
    def minOperationsMaxProfit(self, customers, boardingCost, runningCost):
        res = 0
        maxProfit = 0
        remain = 0
        profit = 0
        cnt = 0
        for c in customers:
            cnt += 1
            remain += c
            if remain >= 4:
                curr = 4
                remain -= 4
            else:
                curr = remain
                remain = 0
            profit += curr * boardingCost - runningCost
            if profit > maxProfit:
                maxProfit = profit
                res = cnt
        while remain > 0:
            cnt += 1
            if remain >= 4:
                curr = 4
                remain -= 4
            else:
                curr = remain
                remain = 0
            profit += curr * boardingCost - runningCost
            if profit > maxProfit:
                maxProfit = profit
                res = cnt
        return res if maxProfit > 0 else -1

test = Solution()
print test.minOperationsMaxProfit([8,3], 5, 6)
print test.minOperationsMaxProfit([10,9,6], 6, 4)
print test.minOperationsMaxProfit([3,4,0,5,1], 1, 92)
print test.minOperationsMaxProfit([10,10,6,4,7], 3, 8)
print test.minOperationsMaxProfit([10,10,1,0,0], 4, 4)