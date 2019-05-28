# -*- coding: utf-8 -*-
# Wiggle Sort I
# 如果i是奇数，nums[i] >= nums[i - 1]
# 如果i是偶数，nums[i] <= nums[i - 1]
# 不满足上述条件交换就行了
class Solution(object):
    def wiggleSort(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] % 2 != 0 and nums[i] <= nums[i - 1] or nums[i] % 2 == 0 and nums[i] > nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
        return nums

test = Solution()
print test.wiggleSort([1, 5, 1, 1, 6, 4])