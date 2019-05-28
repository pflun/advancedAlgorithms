# -*- coding: utf-8 -*-
# 考虑输入stream的话，用iter(),
# while True:
#   try:
#       val = next()
#   except:
#       break
# 最大堆，因为要pop出来最大的
import heapq
class Solution(object):
    def kClosest(self, points, K):
        res = []
        vals = iter(points)
        heap = []
        heapq.heapify(heap)
        val = next(vals)
        while True:
            try:
                d = self.distanceToOrigin(val)
                if len(heap) < K:
                    heapq.heappush(heap, [-d, val])
                else:
                    heapq.heappushpop(heap, [-d, val])
                val = next(vals)
            except StopIteration:
                break
        for point in heap:
            res.append(point[1])
        return res

    def distanceToOrigin(self, point):
        return point[0] * point[0] + point[1] * point[1]

test = Solution()
print test.kClosest([[3,3],[5,-1],[-2,4]], 2)