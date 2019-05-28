# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=v5Ni_3bHjzk
# State = [UNKNOWN, VISITING, SAFE, UNSAFE]
class Solution(object):
    def eventualSafeNodes(self, graph):
        self.res = []
        self.states = ["UNKNOWN"] * len(graph)

        def dfs(graph, curr):
            # 遇到visiting表示有环
            if self.states[curr] == "VISITING":
                return "UNSAFE"
            # 已经是safe/unsafe直接返回
            elif self.states[curr] != "UNKNOWN":
                return self.states[curr]
            # 没访问过标记成visiting
            self.states[curr] = "VISITING"
            # 对于下一步可以走到的节点，如果可以走到unsafe，就把当前节点标记成unsafe
            for next in graph[curr]:
                if dfs(graph, next) == "UNSAFE":
                    self.states[curr] = "UNSAFE"
                    return "UNSAFE"
            # 走不到unsafe，那么当前节点就是safe
            self.states[curr] = "SAFE"
            return "SAFE"

        for i in range(len(graph)):
            if dfs(graph, i) == "SAFE":
                self.res.append(i)

        return sorted(self.res)

test = Solution()
print test.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]])