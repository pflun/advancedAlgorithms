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

    def kSmallestPairs2(self, nums1, nums2, k):
        heap = []
        heapq.heapify(heap)
        for a in nums1:
            for b in nums2:
                if len(heap) < k:
                    heapq.heappush(heap, [-(a+b), a, b])
                else:
                    if heap and -heap[0][0] > a + b:
                        heapq.heappushpop(heap, [-(a+b), a, b])
                    else:
                        # sorted, pruning
                        break

        return [[h[1], h[2]] for h in heap]

    def kSmallestPairs3(self, nums1, nums2, k):
        # min heap, sum + idx1 + idx2
        heap = [[nums1[0] + nums2[0], 0, 0]]
        heapq.heapify(heap)
        visited = set()
        res = []
        for _ in range(k):
            _, idx1, idx2 = heapq.heappop(heap)
            res.append(([nums1[idx1], nums2[idx2]]))
            if idx1 + 1 < len(nums1) and (idx1 + 1, idx2) not in visited:
                heapq.heappush(heap, [nums1[idx1 + 1] + nums2[idx2], idx1 + 1, idx2])
                visited.add((idx1 + 1, idx2))
            if idx2 + 1 < len(nums2) and (idx1, idx2 + 1) not in visited:
                heapq.heappush(heap, [nums1[idx1] + nums2[idx2 + 1], idx1, idx2 + 1])
                visited.add((idx1, idx2 + 1))
        return res

test = Solution()
print test.kSmallestPairs([1,7,11], [2,4,6], 3)
# print test.kSmallestPairs([1,2], [3], 3)