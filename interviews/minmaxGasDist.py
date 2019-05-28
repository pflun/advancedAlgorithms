# -*- coding: utf-8 -*-
# Replace gatStation with warehouse :)
# heap, DP and binary search
# 不在意具体插在哪（插的具体坐标）以免过早切成更多interval，而是记录每个interval里插了几个
# 最小化 interval处以“插了几个” 这个值
from __future__ import division
import heapq
class Solution(object):
    def minmaxGasDist(self, stations, K):
        heap = []
        heapq.heapify(heap)

        for i in range(len(stations) - 1):
            heapq.heappush(heap, [self.negativify(stations[i + 1] - stations[i]), 1])

        while K > 0:
            space, insertNum = heap[0]
            space = self.negativify(space)
            heapq.heappop(heap)
            heapq.heappush(heap, [self.negativify(space * insertNum / (insertNum + 1)), insertNum + 1])
            K -= 1

        return self.negativify(heap[0][0])

    def negativify(self, n):
        n = -n
        return n

test = Solution()
print test.minmaxGasDist([10, 19, 25, 27, 56, 63, 70, 87, 96, 97], 3)