# -*- coding: utf-8 -*-
# union find
class Solution(object):
    def __init__(self):
        self.dic = {}
    def equationsPossible(self, equations):
        # Union '=='
        for eq in equations:
            x, sign, y = eq[0], eq[1], eq[-1]
            if sign == "=":
                self.build(x, y)

        # 验证!=
        for eq in equations:
            x, sign, y = eq[0], eq[1], eq[-1]
            # 不在dic里不需要验证
            if sign == "!" and x in self.dic and y in self.dic:
                px, py = self.find(x), self.find(y)
                if px == py:
                    return False
        return True

    # O(n) 返回老大哥
    def find(self, x):
        parent = self.dic[x]
        while parent != self.dic[parent]:
            parent = self.dic[parent]
        return parent

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.dic[py] = px
        return

    def build(self, child, parent):
        self.dic[child] = parent
        # dic[老大哥] = 老大哥
        if parent not in self.dic:
            self.dic[parent] = parent

test = Solution()
print test.equationsPossible(["c==c","b==d","x!=z"])