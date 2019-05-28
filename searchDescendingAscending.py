# -*- coding: utf-8 -*-
# 从一个递减再递增的数组中找target number。解法：先binarySearch找valley number，然后两边分别找target number
class Solution(object):
    def searchDescendingAscending(self, nums, target):
        valley = float('inf')

        # binary search
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) / 2
            valley = min(valley, nums[mid])
            if nums[mid] < nums[mid + 1] and nums[mid] < nums[mid - 1]:
                break
            if nums[mid] > nums[mid - 1]:
                right = mid
            elif nums[mid] > nums[mid + 1]:
                left = mid

        descend = self.binarySearch(nums[:mid], target)
        ascend = self.binarySearch(nums[mid:], target)
        # print mid, nums[:mid], nums[mid:]

        if descend == -1 and ascend == -1:
            return -1
        elif descend == -1:
            # 因为穿进ascend是后半部分数组，所以返回的只是后半部分的index，这是需要加上前半部分的长度也就是mid
            return ascend + mid
        else:
            return ascend

    def binarySearch(self, arr, x):
        # binary search
        left, right = 0, len(arr) - 1
        while left + 1 < right:
            mid = (left + right) / 2
            if arr[mid] < x:
                left = mid
            else:
                right = mid
        if arr[left] == x:
            return left
        elif arr[right] == x:
            return right
        return -1

test = Solution()
print test.searchDescendingAscending([7, 5, 3, 1, 2, 4, 6, 8, 10, 12], 2)