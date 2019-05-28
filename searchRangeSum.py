# -*- coding: utf-8 -*-
# 给了一个排序的数组，然后给出一个range(比如说[low, high]），求这个数组里的数在这个range之间的和。
# 比如说数组是[1，3，5，7，9], 然后range是[4,7],返回的结果是12（5+7）。
class Solution(object):
    def searchRangeSum(self, arr, low, high):
        res = 0
        lower = self.binaryLower(arr, low)
        upper = self.binaryUpper(arr, high)

        for i in range(lower, upper + 1):
            res += arr[i]

        return res

    def binaryLower(self, arr, x):
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

        return right

    def binaryUpper(self, arr, x):
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

        return left

test = Solution()
print test.searchRangeSum([0, 1, 2, 4, 5, 6, 7], 3, 5)