# -*- coding: utf-8 -*-
class Solution(object):
    def slidingWindowSum(self, nums, k):
        if k > len(nums):
            return []
        res = []
        sum = 0
        for i in range(k):
            sum += i
        res.append(sum)
        for i in range(k, len(nums)):
            sum -= nums[i - k]
            sum += nums[i]
            res.append(sum)

        return res


test = Solution()
print test.slidingWindowSum([1,3,-1,-3,5,3,6,7], 3)