# -*- coding: utf-8 -*-
# min heap with negative largest element on the top (取反， 就相当于最大堆，堆顶存的是当前最大pair。对于剩下的pairs，与堆顶比较后压入或扔掉)
#   -7
# -3  -5
import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        res = []
        heap = []
        heapq.heapify(heap)

        for n1 in nums1:
            for n2 in nums2:
                if len(heap) < k:
                    heapq.heappush(heap, (-n1 - n2, [n1, n2]))
                else:
                    if heap and -heap[0][0] > n1 + n2:
                        heapq.heappop(heap)
                        heapq.heappush(heap, (-n1 - n2, [n1, n2]))
                    else:
                        break
        counter = 0
        while counter < k and heap:
            res.append(heapq.heappop(heap)[1])
            counter += 1

        # Or return [heapq.heappop(heap)[1] for _ in range(k) if heap]
        return res

test = Solution()
print test.kSmallestPairs([1,7,11], [2,4,6], 3)
# print test.kSmallestPairs([1,2], [3], 3)