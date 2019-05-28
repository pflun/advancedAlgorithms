# -*- coding: utf-8 -*-
# i.e. [4,3,2,1,0]
# 维护一个最远能到达的位置, 上面第一个4所在的块至少要包括i=4，不然如果中间断开4就跑不到i=4的位置了
class Solution(object):
    def maxChunksToSorted(self, arr):
        currMax = 0
        cnt = 0
        for i in range(len(arr)):
            currMax = max(currMax, arr[i])
            if currMax == i:
                cnt += 1
        return cnt

test = Solution()
print test.maxChunksToSorted([1,0,2,3,4])