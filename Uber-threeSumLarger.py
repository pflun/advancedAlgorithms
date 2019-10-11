# -*- coding: utf-8 -*-
# 一个给定array， 找所有三元素组满足和大于某threshold
# sample: [2,1,3,0,3], 5
# output: 5
# description:
# [0,3,3]
# [1,3,3]
# [1,2,3]
# [1,2,3]
# [2,3,3]
class Solution(object):
    def threeSumLarger(self, nums, T):
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] <= T:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    #k -= 1
                    j += 1
        return res

test = Solution()
print test.threeSumLarger([2,1,3,0,3], 5)