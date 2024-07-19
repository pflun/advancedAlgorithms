# -*- coding: utf-8 -*-
# greedy cost高的尽早先切
import heapq
class Solution(object):
    def minimumCost(self, m, n, horizontalCut, verticalCut):
        # horizontal/vertical切的系数
        h = 1
        v = 1
        res = 0
        heap = []
        heapq.heapify(heap)
        for c in horizontalCut:
            heapq.heappush(heap, [-c, 'h'])
        for c in verticalCut:
            heapq.heappush(heap, [-c, 'v'])
        while heap:
            cost, dir = heapq.heappop(heap)
            cost = -cost
            # 如果该切横刀，下一次需要切的纵刀数量加一
            # res += 横刀cost * 横刀要切的次数
            if dir == 'h':
                res += cost * h
                v += 1
            elif dir == 'v':
                res += cost * v
                h += 1
        return  res

test = Solution()
print test.minimumCost(3, 2, [1,3], [5])
print test.minimumCost(2, 2, [7], [4])