# -*- coding: utf-8 -*-
# 给你一个数组，和一个function accept(), 找到数组中最大的可以accept的值
class Solution(object):
    def largestCanAccept(self, arr):
        low = 0
        high = len(arr) - 1
        while low < high:
            mid = (low + high) / 2
            print mid
            if self.accept(arr[mid]):
                low = mid
            else:
                high = mid - 1
        return arr[low] if self.accept(arr[low]) else None

    # i.e., accept less than 8
    def accept(self, n):
        return True if n < 8 else False


test = Solution()
print test.largestCanAccept([1,3,7,9,10])