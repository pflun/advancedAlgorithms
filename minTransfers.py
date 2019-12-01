# -*- coding: utf-8 -*-
# 等等，这题貌似不是priority queue?
import heapq
class Solution(object):
    def minTransfers(self, transactions):
        res = 0
        dic = {}
        for t in transactions:
            x, y, z = t[0], t[1], t[2]
            dic[x] = dic.get(x, 0) - z
            dic[y] = dic.get(y, 0) + z
        positive = []
        negative = []
        heapq.heapify(positive)
        heapq.heapify(negative)
        for v in dic.values():
            if v > 0:
                heapq.heappush(positive, -v)
            elif v < 0:
                heapq.heappush(negative, v)
        while positive and negative:
            currP = -heapq.heappop(positive)
            currN = heapq.heappop(negative)
            remain = currP + currN
            if remain > 0:
                heapq.heappush(positive, -remain)
            elif remain < 0:
                heapq.heappush(negative, remain)
            res += 1
        return res

test = Solution()
print test.minTransfers([[0,1,10], [1,0,1], [1,2,5], [2,0,5]])
print test.minTransfers([[0,1,10], [2,0,5]])
print test.minTransfers([[1, 8, 1], [1, 9, 1], [2, 8, 10], [3, 9, 20], [4, 10, 30], [5, 11, 40], [6, 12, 50], [7, 13, 60], [20, 80, 10], [30, 90, 20], [40, 100, 30], [50, 110, 40], [60, 120, 50], [70, 130, 60]])