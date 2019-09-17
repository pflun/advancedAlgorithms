# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=r6Wz4W1TbuI
# 二维DP，生成len(nums) * 从正到负sum(nums)的矩阵，dp[i][j]代表用前i个数达到j值时有多少ways
# 当前cell只能从上一行的两个位置得到，分别是-nums[i]和+nums[i]的位置
class Solution(object):
    def findTargetSumWays(self, nums, S):
        maxVal = sum(nums)
        dp = [[None for _ in range(2 * maxVal + 1)] for _ in range(len(nums) + 1)]
        offset = maxVal
        dp[0][offset] = 1

        for i in range(1, len(nums) + 1):
            for j in range(2 * maxVal + 1):
                if j - nums[i - 1] >= 0 and dp[i - 1][j - nums[i - 1]]:
                    left = dp[i - 1][j - nums[i - 1]]
                else:
                    left = 0
                if j + nums[i - 1] < 2 * maxVal + 1 and dp[i - 1][j + nums[i - 1]]:
                    right = dp[i - 1][j + nums[i - 1]]
                else:
                    right = 0
                dp[i][j] = left + right

        return dp[-1][S + offset] if dp[-1][S + offset] else -1

test = Solution()
print test.findTargetSumWays([1, 1, 1, 1, 1], 3)

