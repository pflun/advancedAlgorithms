# -*- coding: utf-8 -*-
# 输入moveCost适合正着填dp，就每次往下一层尝试填更小值，注意别忘加cell本身value
class Solution(object):
    def minPathCost(self, grid, moveCost):
        res = float('inf')
        dp = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(dp[0])):
            dp[0][i] = 0
        for i in range(len(grid) - 1):
            for j in range(len((grid[0]))):
                currVal = grid[i][j]
                currCost = dp[i][j]
                for k in range(len(moveCost[currVal])):
                    dp[i + 1][k] = min(dp[i + 1][k], currCost + moveCost[currVal][k] + currVal)
        # 加最后一行cell本身value
        for i in range(len(grid[0])):
            res = min(res, dp[-1][i] + grid[-1][i])
        return res

test = Solution()
print test.minPathCost([[5,3],[4,0],[2,1]], [[9,8],[1,5],[10,12],[18,6],[2,4],[14,3]])
print test.minPathCost([[5,1,2],[4,0,3]], [[12,10,15],[20,23,8],[21,7,1],[8,1,13],[9,10,25],[5,3,2]])