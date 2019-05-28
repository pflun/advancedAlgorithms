# -*- coding: utf-8 -*-
# https://www.cnblogs.com/grandyang/p/8850299.html
# II是I的generalized解法，先把整个数组排序，sum(可以拆分的一块儿) = sum(这块在排序后数组里的对应位置的那块)
class Solution(object):
    def maxChunksToSorted(self, arr):
        sortedArr = sorted(arr)
        res = 0
        sumVal = 0
        prevIdx = 0
        for i in range(len(arr)):
            sumVal += arr[i]
            if sumVal == sum(sortedArr[prevIdx:i + 1]):
                res += 1
                sumVal = 0
                prevIdx = i + 1
        return res

test = Solution()
print test.maxChunksToSorted([2,1,4,3,4])