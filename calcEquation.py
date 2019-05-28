# -*- coding: utf-8 -*-
# Graph + DFS
# https://www.youtube.com/watch?v=UwpvInpgFmo
# A / B = 2.0, 在图里就是 A node 到 B node 的距离是 2.0， B node 到 A node 距离是 0.5， A node 到自己是 1.0
class Solution(object):
    def calcEquation(self, equations, values, queries):
        graph = {}
        for i in range(len(equations)):
            A = equations[i][0]
            B = equations[i][1]
            distance = values[i]
            if A not in graph:
                subDict = {B: distance}
                graph[A] = subDict
            else:
                graph[A][B] = distance
            if B not in graph:
                subDict = {A: 1.0 / distance}
                graph[B] = subDict
            else:
                graph[B][A] = 1.0 / distance

        res = []
        for pair in queries:
            A = pair[0]
            B = pair[1]
            # graph里不存在
            if A not in graph or B not in graph:
                res.append(-1.0)
                continue
            visited = set()
            # DFS找从A -> B
            res.append(self.dfs(A, B, graph, visited))

        return res

    # get result of A / B
    def dfs(self, A, B, graph, visited):
        # 找到B
        if A == B:
            return 1.0
        visited.add(A)
        # retrieve A's neighbors from graph
        for k, v in graph[A].items():
            C = k
            if C in visited:
                continue
            # 从中间点C 继续找B，比如 A -> C -> B
            # distance = C / B
            distance = self.dfs(C, B, graph, visited)
            # A / B = C / B * A / C
            return distance * graph[A][C]
        return -1.0

test1 = Solution()
print test1.calcEquation([ ["a", "b"], ["b", "c"] ], [2.0, 3.0], [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ])