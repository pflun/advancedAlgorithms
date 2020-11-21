# -*- coding: utf-8 -*-
import heapq

class Solution(object):
    # Bellman-Ford, similar to DP
    def networkDelayTime(self, times, N, K):
        # dp[i] is the minimum network latency from K to i, init with maximum
        dp = [float('inf') for _ in range(N)]
        dp[K - 1] = 0
        for _ in range(N):
            for t in times:
                u, v, w = t[0] - 1, t[1] - 1, t[2]
                dp[v] = min(dp[v], dp[u] + w)
        return -1 if max(dp) == float('inf') else max(dp)

    # Dijkstra, 总能保证每个新节点第一次出heap是最短的(min heap)
    def networkDelayTime2(self, times, N, K):
        weight = {i: {} for i in range(N + 1)}
        for u, v, w in times:
            weight[u][v] = w
        heap = [(0, K)]
        # each distance from K
        dic = {}
        while heap:
            time, u = heapq.heappop(heap)
            if u not in dic:
                dic[u] = time
                if u in weight:
                    for v in weight[u].keys():
                        # (K到u + u到v， 下次从v继续找)，这样总能保证heap里多个到v的路径里，最短的先pop出heap
                        heapq.heappush(heap, (dic[u] + weight[u][v], v))
        return max(dic.values()) if len(dic) == N else -1

test = Solution()
print test.networkDelayTime2([[1,2,1]], 2, 2)
print test.networkDelayTime2([[2,1,1],[2,3,1],[3,4,1]], 4, 2)
print test.networkDelayTime2([[2,1,1],[2,3,1],[3,4,2],[2,4,3],[1,4,1]], 4, 2)
print test.networkDelayTime([[1,2,1],[2,1,3]], 2, 2)