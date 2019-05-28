# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=7DKFpWnaxLI
# dp[i]: 以当前i为结尾（必须用到i）的increasing子序列最大长度，求dp[len(nums)]
# if curr > 某个以prev结尾的, 那么就意味着curr结尾的最大长度就是这个dp[prev] + 1, 1就是curr，当然dp[curr]要max所有的dp[prev]
class Solution(object):
    def lengthOfLIS(self, nums):
        res = 0
        dp = [1] * len(nums)
        dp[0] = 1

        for i in range(1, len(nums)):
            for j in range(0, i):
                # if curr > (one of) prev, dp_curr = dp_prev + 1, max through all prevs
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        for i in dp:
            res = max(res, i)

        return res

test = Solution()
print test.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])