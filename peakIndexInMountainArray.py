# -*- coding: utf-8 -*-
class Solution(object):
    # https://leetcode.com/problems/peak-index-in-a-mountain-array/solutions/139849/
    def peakIndexInMountainArray2(self, arr):
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = (left + right) / 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left

    # Binary Search, bug
    def peakIndexInMountainArray2(self, arr):
        left = 0
        right = len(arr) - 1
        while left + 1 < right:
            mid = (left + right) / 2
            if arr[mid] > arr[left] and arr[mid] > arr[right]:
                return mid
            elif arr[left] < arr[mid] < arr[right]:
                left = mid
            else:
                right = mid

    # 原题是definitely a mountain，我还多写了检查单调递增和单调递减
    def peakIndexInMountainArray(self, A):
        idx = 0
        flag = 1

        for i in range(len(A) - 1):
            if A[i] < A[i + 1] and flag == 1:
                idx = i + 1
            elif A[i] >= A[i + 1] and flag == 1:
                flag = 0
            elif flag == 0:
                if A[i] <= A[i + 1]:
                    return False

        return idx

test = Solution()
print test.peakIndexInMountainArray2([0,2,1,0])