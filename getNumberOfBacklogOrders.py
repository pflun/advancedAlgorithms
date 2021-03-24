# Wish Trading System
import heapq
class Solution(object):
    def getNumberOfBacklogOrders(self, orders):
        # max heap
        buys = []
        # min heap
        sells = []
        heapq.heapify(buys)
        heapq.heapify(sells)
        for o in orders:
            price = o[0]
            amount = o[1]
            type = o[2]
            # sell
            if type == 1:
                heapq.heappush(sells, [price, amount])
            elif type == 0:
                heapq.heappush(buys, [-price, amount])
            while len(buys) != 0 and len(sells) != 0 and -buys[0][0] >= sells[0][0]:
                buyOrder = heapq.heappop(buys)
                sellOrder = heapq.heappop(sells)
                buyPrice, buyAmount = -buyOrder[0], buyOrder[1]
                sellPrice, sellAmount = sellOrder[0], sellOrder[1]

                if buyAmount == sellAmount:
                    continue
                elif buyAmount > sellAmount:
                    heapq.heappush(buys, [-buyPrice, buyAmount - sellAmount])
                elif buyAmount < sellAmount:
                    heapq.heappush(sells, [sellPrice, sellAmount - buyAmount])

        cnt = 0
        while buys:
            cnt += heapq.heappop(buys)[1]
        while  sells:
            cnt += heapq.heappop(sells)[1]
        return cnt % (10 ** 9 + 7)

test = Solution()
print test.getNumberOfBacklogOrders([[10,5,0],[15,2,1],[25,1,1],[30,4,0]])
print test.getNumberOfBacklogOrders([[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]])
