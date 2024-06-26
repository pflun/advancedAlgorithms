# -*- coding: utf-8 -*-
class Solution(object):
    # binarysearchtemplate.py
    def searchRange3(self, nums, target):

        def lower_bound(arr, x):
            l = 0
            r = len(arr)
            while l < r:
                m = (l + r) / 2
                if arr[m] >= x:
                    r = m
                else:
                    l = m + 1
            return l

        def upper_bound(arr, x):
            l = 0
            r = len(arr)
            while l < r:
                m = (l + r) / 2
                if arr[m] > x:
                    r = m
                else:
                    l = m + 1
            return l

        if not nums:
            return [-1, -1]
        left = lower_bound(nums, target)
        if left < 0 or left >= len(nums) or nums[left] != target:
            return [-1, -1]
        else:
            return [left, upper_bound(nums, target) - 1]

    def searchRange2(self, nums, target):
        # find first element larger than target
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) / 2
            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid
        upperBound = low - 1

        # first element smaller
        low = 0
        high = len(nums) - 1
        while low + 1 < high:
            mid = (low + high) / 2
            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid
        lowerBound = high + 1
        if lowerBound == 0 or upperBound == 0:
            return [-1, -1]
        else:
            return [lowerBound, upperBound]

    def searchRange(self, nums, target):
        res = []
        start = 0
        end = len(nums) - 1

        # binary search find first target from left
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] == target:
                res.append(mid)
                break
            elif nums[mid] > target:
                end = mid
            else:
                start = mid

        # target not found
        if len(res) == 0:
            return [-1, -1]

        # binary search find first larger than target
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) / 2
            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid

        # first larger index - 1 is the last target index
        if low - 1 == res[0]:
            return res
        # append last target index
        elif low - 1 > res[0]:
            return res + [low - 1]

test = Solution()
print test.searchRange3([5,7,7,8,8,10], 8)
# print test.searchRange2([5,7,7,8,8,10], 6)
print test.searchRange3([2,2], 3)