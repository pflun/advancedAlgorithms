# -*- coding: utf-8 -*-
# 连通区域个数 - 1
class Solution(object):
    def makeConnected(self, n, connections):
        if n > len(connections) + 1:
            return -1

        dic = {}
        for i in range(n):
            dic[i] = i

        def find(x):
            parent = dic[x]
            while parent != dic[parent]:
                parent = dic[parent]
            return parent

        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                dic[px] = py

        for i in range(len(connections)):
            union(connections[i][0], connections[i][1])

        res = -1
        for k, v in dic.items():
            if k == v:
                res += 1
        return res

test = Solution()
print test.makeConnected(4, [[0,1],[0,2],[1,2]])
print test.makeConnected(6, [[0,1],[0,2],[0,3],[1,2],[1,3]])
print test.makeConnected(6, [[0,1],[0,2],[0,3],[1,2]])
print test.makeConnected(5, [[0,1],[0,2],[3,4],[2,3]])