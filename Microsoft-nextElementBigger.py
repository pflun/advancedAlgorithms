# -*- coding: utf-8 -*-
# input: list of int, output: list of distance (从curr到curr右侧第一个比curr大的元素的距离，没有大的就是0)
class Solution(object):
    def nextElementBigger(self, arr):
        res = []
        for i in range(len(arr)):
            res.append(self.findNext(arr, i))

        return res

    def findNext(self, arr, i):
        if i + 1 == len(arr):
            return 0
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[i]:
                return j - i

        return 0

test1 = Solution()
print test1.nextElementBigger([2,5,3,4,7,23,15,7,16,25])