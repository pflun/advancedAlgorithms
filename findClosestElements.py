# -*- coding: utf-8 -*-
class Solution(object):
    def findClosestElements(self, arr, k, x):
        res = []

        index = self.binarySearch(arr, x)

        start = index - 1
        end = index

        # 从target的index左右开始向两端扫
        while start >= 0 and end <= len(arr):
            if abs(arr[start] - x) <= abs(arr[end] - x):
                res.append(arr[start])
                start -= 1
            else:
                res.append(arr[end])
                end += 1
            if len(res) == k:
                res.sort()
                return res

        # edge case when start reach the edge of arr
        while start >= 0:
            res.append(res[end])
            end += 1
            if len(res) == k:
                res.sort()
                return res

        # edge case when end reach the edge of arr
        while end <= len(arr):
            res.append(res[start])
            start -= 1
            if len(res) == k:
                res.sort()
                return res

        return res

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
print test.findClosestElements([1,2,3,4,5], 4, 3)

# Need debug, edge case index out of range, start = index - 1 which index can be -1