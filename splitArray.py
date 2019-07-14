# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=_k-Jb4b7b_0&t=169s
# Chocolate sweetness 同理
# You friends are greedy so they will always take the highest sweetness sum. Find out what is the maximum sweetness level you could get.
class Solution(object):
    def splitArray(self, nums, m):
        dp = [[float('inf')] * len(nums) for _ in range(m + 1)]
        # init 只划分成1组
        for i in range(len(nums)):
            dp[1][i] = sum(nums[:i])

        for i in range(2, m + 1):
            for j in range(i - 1, len(nums)):
                # k 分割点
                for k in range(j):
                    dp[i][j] = min(dp[i][j], max(dp[i - 1][k], sum(nums[k:])))
        return dp[m][len(nums) - 1]

test = Solution()
print test.splitArray([7,2,5,10,8], 2)