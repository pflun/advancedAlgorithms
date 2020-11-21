# -*- coding: utf-8 -*-
import heapq
class Solution(object):
    # Dijkstra, 下面代码和模板的区别是，模板每次用了最短dic[u]以后不能保证这个最短的步数是否小于当前pop出来的step
    # 所以把模板dic删掉每次用当前price + weight[u][v]就行
    def findCheapestPrice2(self, n, flights, src, dst, K):
        weight = {i: {} for i in range(n)}
        for f in flights:
            u, v, w = f[0], f[1], f[2]
            weight[u][v] = w
        # price, city, step
        heap = [(0, src, 0)]
        heapq.heapify(heap)
        while heap:
            price, u, step = heapq.heappop(heap)
            # found
            if u == dst:
                return price
            # within K stops, A => B => C means 1 stop
            if step <= K:
                if u in weight:
                    for v in weight[u].keys():
                        heapq.heappush(heap, (price + weight[u][v], v, step + 1))
        return -1

    def findCheapestPrice(self, n, flights, src, dst, K):
        self.res = float('inf')
        # stop1 => [[stop2, price], [stop3, price]]
        dic = {}
        for i in range(n):
            dic[i] = []
        for f in flights:
            s, d, p = f[0], f[1], f[2]
            dic[s].append([d, p])
        queue = [[src, 0]]
        step = 0
        while queue:
            if step > K + 1:
                break
            size = len(queue)
            for _ in range(size):
                curr, tmp = queue.pop(0)
                if curr == dst:
                    self.res = min(self.res, tmp)
                for next in dic[curr]:
                    stop, price = next[0], next[1]
                    queue.append([stop, tmp + price])

            step += 1
        return self.res

test = Solution()
# print test.findCheapestPrice2(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1)
print test.findCheapestPrice2(4, [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], 0, 3, 1)