# -*- coding: utf-8 -*-
# 对于dp每个cell，保存当前Max和Min
class Solution(object):
    def maxProductPath(self, grid):
        dp = [[(0, 0) for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dp[0][0] = (grid[0][0], grid[0][0])
        for j in range(1, len(grid[0])):
            prevMax, prevMin = dp[0][j - 1]
            dp[0][j] = (prevMax * grid[0][j], prevMax * grid[0][j])
        for i in range(1, len(grid)):
            prevMax, prevMin = dp[i - 1][0]
            dp[i][0] = (prevMax * grid[i][0], prevMax * grid[i][0])
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                leftMax, leftMin = dp[i][j - 1]
                upMax, upMin = dp[i - 1][j]
                currVal = grid[i][j]
                if currVal > 0:
                    currMax = max(leftMax * currVal, upMax * currVal)
                    currMin = min(leftMin * currVal, upMin * currVal)
                else:
                    currMax = max(leftMin * currVal, upMin * currVal)
                    currMin = min(leftMax * currVal, upMax * currVal)
                dp[i][j] = (currMax, currMin)
        resMax, resMin = dp[-1][-1]
        if resMax < 0:
            return -1
        else:
            return resMax % (10 ** 9 + 7)

test= Solution()
print test.maxProductPath(
    [[1,-2,1],
    [1,-2,1],
    [3,-4,1]])