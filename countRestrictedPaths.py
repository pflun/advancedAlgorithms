# -*- coding: utf-8 -*-
# "if dis[next] > dis[curr]"所以dfs不会死循环，A点求解B，B点不会反过来求解A
import heapq
class Solution(object):
    def countRestrictedPaths(self, n, edges):
        self.weight = {i: {} for i in range(1, n + 1)}
        for u, v, w in edges:
            self.weight[u][v] = w
            self.weight[v][u] = w
        heap = [(0, n)]
        self.dic = {}
        while heap:
            time, u = heapq.heappop(heap)
            if u not in self.dic:
                self.dic[u] = time
                if u in self.weight:
                    for v in self.weight[u].keys():
                        heapq.heappush(heap, (self.dic[u] + self.weight[u][v], v))

        memo = [-1 for _ in range(n + 1)]

        return self.dfs(memo, self.dic, self.weight, n)

    def dfs(self, memo, dis, adj, curr):
        if curr == 1:
            return 1
        if memo[curr] != -1:
            return memo[curr]
        res = 0
        if curr in adj:
            for next in adj[curr].keys():
                if dis[next] > dis[curr]:
                    res = (res + self.dfs(memo, dis, adj, next)) % (10 ** 9 + 7)
        memo[curr] = res
        return res

test = Solution()
print test.countRestrictedPaths(5, [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]])
print test.countRestrictedPaths(7, [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]])
# TLE
# def dfs(A, B, visited):
#     if A == B:
#          self.res += 1
#     visited.add(A)
#     for k in self.weight[A].keys():
#         if k not in visited and self.dic[A] > self.dic[k]:
#             dfs(k, B, visited)
#     visited.remove(A)
# dfs(1, n, set())