# -*- coding: utf-8 -*-
class Solution(object):
    # TLE should use two pointers
    def maximumScore2(self, nums, k):
        dp = [[None for _ in range(len(nums))] for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][i] = nums[i]
            if i > 0:
                dp[0][i] = min(dp[0][i - 1] / i, nums[i]) * (i + 1)
        for i in range(1, len(nums)):
            for j in range(i + 1, len(nums)):
                dp[i][j] = min(dp[i][j - 1] / (j - i), nums[j]) * (j - i + 1)

        res = float('-inf')
        for i in range(k + 1):
            for j in range(k, len(nums)):
                res = max(res, dp[i][j])
        return res

    def maximumScore(self, nums, k):
        i = j = k
        res = nums[k]
        tmpSmall = nums[k]
        while i > 0 or j < len(nums) - 1:
            if i == 0:
                j += 1
            elif j == len(nums) - 1:
                i -= 1
            # 左边小，移动右边才可能更大
            elif nums[i - 1] < nums[j + 1]:
                j += 1
            else:
                i -= 1
            tmpSmall = min(tmpSmall, min(nums[i], nums[j]))
            res = max(res, tmpSmall * (j - i + 1))
        return res

test = Solution()
print test.maximumScore([1,4,3,7,4,5], 3)
print test.maximumScore([5,5,4,5,4,1,1,1], 0)