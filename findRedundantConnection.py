# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=4hJ721ce010
# 684是无向图，用union find，遍历edge，每次把parent付给做节点，若发现母节点相同则为多余
class Solution(object):
    def __init__(self):
        self.dic = {}

    # def build(self, child, parent):
    #     self.dic[child] = parent
    #     # dic[老大哥] = 老大哥
    #     if parent not in self.dic:
    #         self.dic[parent] = parent

    # O(n) 返回老大哥
    def find(self, x):
        parent = self.dic[x]
        while parent != self.dic[parent]:
            parent = self.dic[parent]
        return parent

    # def union(self, x, y):
    #     rootx = self.find(x)
    #     rooty = self.find(y)
    #     if rootx == rooty:
    #         return False
    #     self.dic[rootx] = rooty
    #     return True

    def findRedundantConnection(self, edges):
        for e in edges:
            u = e[0]
            v = e[1]
            # 初始化指向自己
            if u not in self.dic:
                self.dic[u] = u
            if v not in self.dic:
                self.dic[v] = v
            pu = self.find(u)
            pv = self.find(v)
            # found circle
            if pu == pv:
                return e, self.dic
            # Union
            else:
                self.dic[pu] = pv

test1 = Solution()
print test1.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]])