# -*- coding: utf-8 -*-
# 给定一个矩形的宽和长，求所有可能的路径数量
# Rules：
# 1. 从左上角走到右上角
# 2. 机器人只能走右上，右和右下;j
# 思路:
# 按照列dp, dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1] + dp[i + 1][j - 1]， 注意i-1，i+1需要存在

class Solution(object):
    def uniquePaths3(self, m, n):
        dp = [[1 for _ in range(m)] for _ in range(n)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1] + dp[i + 1][j - 1]

        return dp[-1][-1]

# followup1: 优化空间复杂度至 O(n)
# 思路：只保留上一列的空间，用两个数组滚动dp


test = Solution()
print test.uniquePaths3(3, 3)