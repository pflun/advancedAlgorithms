# -*- coding: utf-8 -*-
# Dijkstra + record path history
import heapq
class Solution(object):
    def findAnswer(self, n, edges):
        weight = {i: {} for i in range(n)}
        for e in edges:
            u, v, w = e[0], e[1], e[2]
            weight[u][v] = w
            weight[v][u] = w # Undirected graph
        heap = [(0, 0, [0])]
        heapq.heapify(heap)
        while heap:
            tmpWeights, u, path = heapq.heappop(heap)
            # found
            if u == n - 1:
                # keep pop until found all shortest paths
                allPath = [path]
                while heap and heap[0][0] == tmpWeights:
                    tmpWeights, u, path = heapq.heappop(heap)
                    allPath.append(path)
                res = []
                # create a map for connection between all pairs of nodes on the shortest paths
                allShortestDict = {}
                for path in allPath:
                    for i in range(len(path) - 1):
                        allShortestDict[path[i]] = allShortestDict.get(path[i], []) + [path[i + 1]]
                # for each edge check if it's in allShortestDict, bi-direction
                for e in edges:
                    u, v = e[0], e[1]
                    if u in allShortestDict and v in allShortestDict[u] or v in allShortestDict and u in allShortestDict[v]:
                        res.append(True)
                    else:
                        res.append(False)
                return res
            if u in weight:
                for v in weight[u].keys():
                    # bi-direction, won't go back
                    if v not in path:
                        heapq.heappush(heap, (tmpWeights + weight[u][v], v, path + [v]))
        return [False for _ in range(len(edges))]

test = Solution()
print test.findAnswer(6, [[0,1,4],[0,2,1],[1,3,2],[1,4,3],[1,5,1],[2,3,1],[3,5,3],[4,5,2]])
print test.findAnswer(4, [[2,0,1],[0,1,1],[0,3,4],[3,2,2]])
print test.findAnswer(6, [[0,2,7],[3,0,2]])