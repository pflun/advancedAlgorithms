# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=9mdoM2dVid8
# 规律：从右往左找第一个nums[i] < nums[i + 1]，再找第一个nums[i] > nums[firstSmall]，然后交换
# 最后把firstSmall + 1的位置以后reverse一下
class Solution(object):
    def nextPermutation(self, nums):
        if len(nums) == 0:
            return
        firstSmall = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                firstSmall = i
                break
        # cannot find, last permutation 743211, return first
        if firstSmall == -1:
            return sorted(nums)

        firstLarge = -1
        for i in range(len(nums) - 1, firstSmall, -1):
            if nums[i] > nums[firstSmall]:
                firstLarge = i
                break
        nums[firstSmall], nums[firstLarge] = nums[firstLarge], nums[firstSmall]
        nums = nums[:firstSmall + 1] + nums[firstSmall + 1:][::-1]
        return nums

test = Solution()
print test.nextPermutation([1,2,7,4,3,1])