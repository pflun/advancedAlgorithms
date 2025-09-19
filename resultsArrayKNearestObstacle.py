# 3275. K-th Nearest Obstacle Queries
import heapq
class Solution(object):
    def resultsArray(self, queries, k):
        # heap size = k
        heap = []
        heapq.heapify(heap)
        res = []
        for q in queries:
            distance = abs(q[0]) + abs(q[1])
            heapq.heappush(heap, -distance)
            if len(heap) < k:
                res.append(-1)
            elif len(heap) == k:
                res.append(-heap[0])
            else:
                heapq.heappop(heap)
                res.append(-heap[0])
        return res

test = Solution()
print test.resultsArray([[1,2],[3,4],[2,3],[-3,0]], 2)
print test.resultsArray([[5,5],[4,4],[3,3]], 1)