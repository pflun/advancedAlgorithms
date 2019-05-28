import heapq
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        maxRatio = 0
        for i in range(K):
            maxRatio = max(maxRatio, wage[i] / quality[i])
        res = reduce(lambda x, maxRatio: x * maxRatio, quality[:K])

        heap = [ -x for x in quality[:K]]
        heapq.heapify(heap)
        for i in range(K, len(quality)):
            tmp = -heap[0]
            if tmp >= quality[i]:
                heapq.heappush(heap, self.negativify(tmp))
            else:
                heapq.heappush(heap, self.negativify(quality[i]))
                tmpRatio = 0
                
                res = min(res, )

    def negativify(self, n):
        n = -n
        return n
