# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=7si0SiXanYw
# Heap不需要存worker，只要存ratio。只能取最大的wage/quality当作所有工人的pay ratio，res = 最大ratio * 当前totalQuality
from __future__ import division
import heapq
class Worker(object):
    def __init__(self, wage, quality):
        self.wage = wage
        self.quality = quality
        self.ratio = wage / quality

class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        res = float('inf')
        totalQuality = 0
        heap = []
        heapq.heapify(heap)
        workers = []
        for i in range(len(quality)):
            worker = Worker(wage[i], quality[i])
            workers.append(worker)
        workers.sort(key=lambda x: x.ratio, reverse=True)

        for w in workers:
            heapq.heappush(heap, self.negativify(w.ratio))
            totalQuality += w.quality
            if len(heap) == K:
                #
                res = min(res, self.negativify(heap[0]) * totalQuality)
            if len(heap) > K:
                totalQuality -= self.negativify(heapq.heappop(heap))
        return res

    def negativify(self, n):
        n = -n
        return n

test = Solution()
print test.mincostToHireWorkers([3,1,10,10,1], [4,8,2,2,7], 3)