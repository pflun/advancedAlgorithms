# -*- coding: utf-8 -*-
# maintain min and subMin，遇到大于subMin的即存在
class Solution(object):
    def increasingTriplet(self, nums):
        if len(nums) < 3:
            return False
        min = float('inf')
        subMin = float('inf')

        for num in nums:
            if num < min:
                min = num
            elif num < subMin:
                subMin = num
            elif subMin < num:
                return True

        return False

test = Solution()
print test.increasingTriplet([3,2,5,6,1,2])