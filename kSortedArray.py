# https://www.geeksforgeeks.org/nearly-sorted-algorithm/
# Given an array of n elements, where each element is at most k away from its target position,
# devise an algorithm that sorts in O(n log k) time
import heapq
class Solution(object):
    def kSortedArray(self, arr, k):
        heap = arr[:k + 1]
        heapq.heapify(heap)
        res = []
        for i in range(k + 1, len(arr)):
            res.append(heapq.heappop(heap))
            heapq.heappush(heap, arr[i])
        while heap:
            res.append(heapq.heappop(heap))
        return res

test = Solution()
print test.kSortedArray([6, 5, 3, 2, 8, 10, 9], 3)
print test.kSortedArray([10, 9, 8, 7, 4, 70, 60, 50], 4)