# -*- coding: utf-8 -*-
# 对于每一个connected component（根据定义横或者纵坐标相等），比如3个石头可以remove两个，最后一个拿不走
# res = 总石头数 - 连通区域个数（最后一个拿不走，所以拿不走的 = 连通区域个数）
class Solution(object):
    def removeStones(self, stones):
        dic = {}
        for i in range(len(stones)):
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

        for i in range(len(stones)):
            for j in range(i, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i, j)
        res = len(stones)
        for k, v in dic.items():
            if k == v:
                res -= 1
        return res

test = Solution()
print test.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]])