class Solution(object):
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
print test.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1)