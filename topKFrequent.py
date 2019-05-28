# -*- coding: utf-8 -*-
# min heap with negative most frequent element on the top (就相当于最大堆，top最大值)
#     -3(1)
# -2(2)  -2(3)
import heapq

class Solution(object):
    def negativify(self, n):
        n = -n
        return n

    def topKFrequent(self, nums, k):
        res = []
        heap = []
        heapq.heapify(heap)
        dic = {}

        for num in nums:
            dic[num] = dic.get(num, 0) + 1

        for key, val in dic.items():
            heapq.heappush(heap, [self.negativify(val), key])

        counter = 0
        while counter < k:
            res.append(heapq.heappop(heap)[1])
            counter += 1

        return res

test = Solution()
print test.topKFrequent([1,1,1,2,2,3,4,3], 3)