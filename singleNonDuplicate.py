# -*- coding: utf-8 -*-
# Single number must have an even index
# 1, 1, 2, 3, 3, 4, 4
# 2之前都是成对的，所以2的index必是偶数
# 更好的方法是binary search （logn）：https://www.youtube.com/watch?v=uJa9Q-05JxY
class Solution(object):
    def singleNonDuplicate(self, nums):
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]
        low = 0
        high = len(nums) - 1
        while low + 1 < high:
            mid = (low + high) / 2
            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    low = mid
                else:
                    high = mid
            else:
                if nums[mid] == nums[mid - 1]:
                    low = mid
                else:
                    high = mid
        if low % 2 == 0:
            if nums[low] == nums[low + 1]:
                return nums[high]
            else:
                return nums[low]
        else:
            if nums[low] == nums[low - 1]:
                return nums[high]
            else:
                return nums[low]

test = Solution()
print test.singleNonDuplicate([1,1,2,3,3,4,4,8,8])