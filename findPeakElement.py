# -*- coding: utf-8 -*-
class Solution(object):
    def findPeakElement(self, nums):
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i

    # log(n), 这道题如果mid不是peak的话 只需要看右边的那个元素是不是大于mid  如果大于mid 那么右边一定会有一个peak  因为如果右边是个递增到结束的数列 那么结尾的那个就是peak 否则就往前找
    def findPeakElement2(self, nums):
        if len(nums) == 1:
            return 0

        if nums[0] > nums[1]:
            return 0
        elif nums[-1] > nums[-2]:
            return len(nums) - 1

        low = 1
        high = len(nums) - 1

        while low <= high:
            mid = (high + low) / 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            elif nums[mid + 1] > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1


test = Solution()
print test.findPeakElement2([1, 2, 3, 4, 5, 2])