# -*- coding: utf-8 -*-
# 所有odd乘以2变成偶数，之后只需要除法就行
# 不停把最大数除以2放进heap里，不停track deviation和minVal就行
import heapq
class Solution(object):
    def minimumDeviation(self, nums):
        heap = []
        heapq.heapify(heap)
        minVal = float('inf')
        for n in nums:
            n = n * 2 if n % 2 == 1 else n
            minVal = min(minVal, n)
            heapq.heappush(heap, -n)
        res = -heap[0] - minVal
        # peek, heap[0] is always the smallest
        # 当最大的数变成odd结束循环，因为这时只能把这数乘以2变大，如果最大数变大只能导致deviation变大(其他数只能越变越小)
        while -heap[0] % 2 == 0:
            curr = -heapq.heappop(heap)
            heapq.heappush(heap, -curr / 2)
            minVal = min(minVal, curr / 2)
            res = min(res, -heap[0] - minVal)

        return res

test = Solution()
print test.minimumDeviation([3,5])