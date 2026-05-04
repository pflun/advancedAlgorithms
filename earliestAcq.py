# -*- coding: utf-8 -*-
class Solution:
    def earliestAcq(self, logs, n):
        self.dic = {}
        logs.sort()
        for log in logs:
            ts = log[0]
            A = log[1]
            B = log[2]
            if self.union(A, B):
                # 一开始有n个独立连通分量，每次有效合并就减1
                n -= 1
                # 直到整个图变成一个连通分量
                if n == 1:
                    return ts
        return -1

    def find(self, x):
        if x not in self.dic:
            self.dic[x] = x
        parent = self.dic[x]
        while parent != self.dic[parent]:
            parent = self.dic[parent]
        return parent

    # True: 有效合并连通分量
    # False: 无效，已经合并在同一个连通分量里
    def union(self, master, branch):
        fa_master = self.find(master)
        fa_branch = self.find(branch)
        if fa_master != fa_branch:
            self.dic[fa_branch] = fa_master
            return True
        return False

test = Solution()
print test.earliestAcq([[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], 6)
print test.earliestAcq([[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], 4)