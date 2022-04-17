import heapq
class Solution(object):
    def maxIceCream(self, costs, coins):
        res = 0
        heap = []
        heapq.heapify(heap)
        for c in costs:
            heapq.heappush(heap, c)
        while heap and coins >= heap[0]:
            curr = heapq.heappop(heap)
            res += 1
            coins -= curr
        return res

test = Solution()
print test.maxIceCream([1,3,2,4,1], 7)
print test.maxIceCream([10,6,8,7,7,8], 5)
print test.maxIceCream([1,6,3,1,2,5], 20)