# -*- coding: utf-8 -*-
# 解法一：自定义compare
# 解法二：heapq.heappush(heap, [abs(point to origin distance), point])
import heapq

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Solution(object):
    def kClosest(self, points, origin, k):
        res = []
        heap = []
        heapq.heapify(heap)

        for point in points:
            if len(heap) == k:
                if self.compare(point, heap[0], origin) > 0:
                    heapq.heappop(heap)
                    heapq.heappush(heap, point)
            else:
                heapq.heappush(heap, point)

        while heap:
            res = [heapq.heappop(heap)] + res

        return res


    def compare(self, a, b, origin):
        diff = self.calDistance(b, origin) - self.calDistance(a, origin)
        if diff == 0:
            diff = b.x - a.x
        if diff == 0:
            diff = b.y - a.y
        return diff

    def calDistance(self, a, b):
        distance = (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y)
        return distance

test1 = Solution()
print test1.kClosest([Point(4, 6), Point(4, 7), Point(4, 4), Point(2, 5), Point(1, 1)], Point(0, 0), 3)