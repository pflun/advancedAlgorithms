# -*- coding: utf-8 -*-
# Hua hua https://www.youtube.com/watch?v=v57lNF2mb_s
# [l, r) => 每次分成三组[l, m) [m] [m + 1, r)
class Solution(object):
    def binarySearch(self, arr, target):
        l = 0
        r = len(arr) - 1
        while l < r:
            m = (l + r) / 2
            # Optional, if found，如果有这行最终没found最后可以return -1
            # if arr[m] == target:
            #     return m
            #
            # 最重要的判断g(m)
            if arr[m] > target:
                r = m
            else:
                l = m + 1
        # 找到最小的l，使得g(m)为True
        return l

    # 找到first element that A[i] >= x
    def lower_bound(self, arr, x):
        l = 0
        r = len(arr)
        while l < r:
            m = (l + r) / 2
            if arr[m] >= x:
                r = m
            else:
                l = m + 1
        return l

    # 找到first element that A[i] > x
    def upper_bound(self, arr, x):
        l = 0
        r = len(arr)
        while l < r:
            m = (l + r) / 2
            if arr[m] > x:
                r = m
            else:
                l = m + 1
        return l

test = Solution()
print test.lower_bound([1, 2, 2, 2, 4, 4, 5], 2)
print test.lower_bound([1, 2, 2, 2, 4, 4, 5], 3)
print test.upper_bound([1, 2, 2, 2, 4, 4, 5], 2)
# return 7 (len arr) 因为arr内没有任何idx的值严格大于5
print test.upper_bound([1, 2, 2, 2, 4, 4, 5], 5)