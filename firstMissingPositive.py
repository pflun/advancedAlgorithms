# -*- coding: utf-8 -*-
# 很奇特的hash思路，因为结果只和(1, n)有关，把(1, n)以外的删掉
# 一个数出现就把这个数对应index的值+n，那么下次哪个值小于n证明这个值的index没出现过
class Solution(object):
    def firstMissingPositive(self, nums):
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0

        for i in range(len(nums)):
            nums[nums[i] % n] += n

        for i in range(1, len(nums)):
            if nums[i] / n == 0:
                return i
        return len(nums)

test = Solution()
print test.firstMissingPositive([3,4,-1,1])