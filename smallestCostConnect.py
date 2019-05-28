# -*- coding: utf-8 -*-
# There are sticks with various lengths in a box. You can connect two sticks at a time,
# and the cost is the total length of two sticks added.
# Write a program to figure out how to minimize the total cost to connect all of the sticks in a box.
# e.g. 1, 3, 4
# 最佳策略是先挑1,3 再挑4
# 總和=(1+3)+(4+4)=12
#
# 如果先挑3,4
# 會變成 (3+4)+(1+7)=15
import heapq
class Solution(object):
    def smallestCostConnect(self, sticks):
        res = 0
        heap = []
        heapq.heapify(heap)
        for s in sticks:
            heapq.heappush(heap, s)
        while len(heap) > 1:
            s1 = heapq.heappop(heap)
            s2 = heapq.heappop(heap)
            res += s1 + s2
            heapq.heappush(heap, s1 + s2)
        return res

test = Solution()
print test.smallestCostConnect([1,3,4])