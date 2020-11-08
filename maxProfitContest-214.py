import heapq
class Solution(object):
    def maxProfit(self, inventory, orders):
        res = 0
        heap = []
        heapq.heapify(heap)
        for a in inventory:
            heapq.heappush(heap, -a)
        while orders > 0:
            orders -= 1
            curr = -heapq.heappop(heap)
            res += curr
            heapq.heappush(heap, -curr + 1)
        return res % (10 ** 9 + 7)

test = Solution()
print test.maxProfit2([2,5], 4)
print test.maxProfit2([3,5], 6)
print test.maxProfit2([2,8,4,10,6], 20)
print test.maxProfit2([1000000000], 1000000000)
print test.maxProfit2([773160767], 252264991)