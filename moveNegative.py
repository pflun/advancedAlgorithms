# -*- coding: utf-8 -*-
# Record the position of left 0, if != 0 then exchange, zero move to next, zero keep stay at left position of zeros

class Solution(object):
    def moveNegative(self, nums):
        ng = 0  # records the position of "0"
        for i in xrange(len(nums)):
            # print i, zero, nums
            # two pointer, right pointer always move but left(zero) pointer stay at left-est zero, exchange when right != 0, left(zero) pointer move to next zero
            if nums[i] < 0:
                nums[i], nums[ng] = nums[ng], nums[i]
                ng += 1

        return nums

test = Solution()
print test.moveNegative([2,0,-1,-3,0,12])