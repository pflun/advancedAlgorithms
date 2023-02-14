class Solution(object):
    def pickGifts(self, gifts, k):
        import math
        import heapq
        heap = []
        heapq.heapify(heap)
        res = 0
        for g in gifts:
            heapq.heappush(heap, -g)
        for _ in range(k):
            curr = -heapq.heappop(heap)
            heapq.heappush(heap, -math.floor(math.sqrt(curr)))
        for h in heap:
            res += h
        return -int(res)