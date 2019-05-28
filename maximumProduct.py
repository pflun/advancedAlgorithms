# -*- coding: utf-8 -*-
class Solution(object):
    def maximumProduct(self, nums):
        length = len(nums)
        nums.sort()
        # 无非是最大三个相乘或两个最小（negative）乘以一个最大
        return max(nums[length - 1] * nums[length - 2] * nums[length - 3], nums[length - 1] * nums[0] * nums[1])

test = Solution()
print test.maximumProduct([1,2,3,4,-20,-22])