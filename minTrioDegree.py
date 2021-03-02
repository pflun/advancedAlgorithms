class Solution(object):
    # somehow TLE
    def minTrioDegree(self, n, edges):
        res = float('inf')
        graph = {}
        for e in edges:
            e1 = e[0]
            e2 = e[1]
            if e1 in graph:
                graph.get(e1).add(e2)
            else:
                graph[e1] = set([e2])
            if e2 in graph:
                graph.get(e2).add(e1)
            else:
                graph[e2] = set([e1])
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                for k in range(j + 1, n + 1):
                    if i not in graph or j not in graph or k not in graph:
                        continue
                    if i in graph[j] and j in graph[i] and j in graph[k] and k in graph[j] and i in graph[k] and k in graph[i]:
                        res = min(res, len(graph[i]) + len(graph[j]) + len(graph[k]) - 6)
        if res == float('inf'):
            return -1
        return res

test = Solution()
print test.minTrioDegree(6, [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]])
print test.minTrioDegree(7, [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]])
# degree needs to connect
print test.minTrioDegree(4, [[1,2],[4,1],[4,2]])
print test.minTrioDegree(6, [[6,5],[4,3],[5,1],[1,4],[2,3],[4,5],[2,6],[1,3]])