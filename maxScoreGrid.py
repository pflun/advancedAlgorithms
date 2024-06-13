# -*- coding: utf-8 -*-
# dp[i][j]: grid[i, j]点左上方区域(不含[i, j])里的最小值
# 当前点[i, j]减去最小值就是能获得的最大值，和路径完全无关(参考example 1，最小5当前14所以是9)
class Solution(object):
    def maxScore(self, grid):
        dp = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(1, len(grid[0])):
            dp[0][i] = min(dp[0][i - 1], grid[0][i - 1])
        for j in range(1, len(grid)):
            dp[j][0] = min(dp[j - 1][0], grid[j - 1][0])
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = min([dp[i - 1][j], dp[i][j - 1], grid[i - 1][j], grid[i][j - 1]])
        res = float('-inf')
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res = max(res, grid[i][j] - dp[i][j])
        return res

test = Solution()
print test.maxScore([[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]])
print test.maxScore([[4,3,2],[3,2,1]])