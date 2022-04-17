import heapq
class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        engineers = []
        for i in range(n):
            engineers.append([efficiency[i], speed[i]])
        # when iteration, the new incoming engineer always have lower efficiency (to * totalSpeed)
        engineers.sort(reverse=True)
        heap = []
        heapq.heapify(heap)
        res = 0
        totalSpeed = 0
        for e in engineers:
            # layoff the engineer that has lowest speed
            if len(heap) == k:
                totalSpeed -= heapq.heappop(heap)
            heapq.heappush(heap, e[1])
            totalSpeed += e[1]
            res = max(res, totalSpeed * e[0])
        return res % (10 ** 9 + 7)