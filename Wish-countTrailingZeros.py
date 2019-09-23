# -*- coding: utf-8 -*-
# 找从右往左连续的0的个数
class Solution(object):
    def countTrailingZeros(self, arr):
        cnt = 0
        res = 0
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == 0:
                cnt += 1
                res = max(res, cnt)
            else:
                cnt = 0
        return res

    # sorted binary search descending
    def countTrailingZeros2(self, arr):
        low = 0
        high = len(arr) - 1
        # idx of first num larger than 0
        while low + 1 < high:
            mid = (low + high) / 2
            if arr[mid] <= 0:
                high = mid - 1
            else:
                low = mid
        if high == 0:
            lower = low
        else:
            lower = high

        left = 0
        right = len(arr) - 1
        while left + 1 < right:
            mid = (left + right) / 2
            if arr[mid] >= 0:
                left = mid + 1
            else:
                right = mid
        if left == 0:
            higher = right
        else:
            higher = left

        # lower is the idx of the prev element of first 0, higher is the idx of the next element of last 0
        return higher - lower

test = Solution()
# print test.countTrailingZeros([1,2,3,0,0,5,0,0,0])
print test.countTrailingZeros2([5,4,3,2,1,1,0,0,0,0,-1,-2])