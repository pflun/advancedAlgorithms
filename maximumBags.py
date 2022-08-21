import heapq
class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        res = 0
        heap = []
        heapq.heapify(heap)
        for i in range(len(capacity)):
            if capacity[i] == rocks[i]:
                res += 1
            elif capacity[i] > rocks[i]:
                heapq.heappush(heap, capacity[i] - rocks[i])

        while heap:
            curr = heapq.heappop(heap)
            if curr <= additionalRocks:
                res += 1
                additionalRocks -= curr
            else:
                break
        return res

test = Solution()
print test.maximumBags([2,3,4,5], [1,2,4,4], 2)
print test.maximumBags([10,2,2], [2,2,0], 100)