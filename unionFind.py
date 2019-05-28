# -*- coding: utf-8 -*-
# 并查集优化，合并路径：A -> B -> C -> D 合并成 A -> D, B -> D, C -> D，这样每次find老大哥只需要O(1)
class Solution:
    def __init__(self):
        self.dic = {}

    def build(self, child, parent):
        self.dic[child] = parent
        # dic[老大哥] = 老大哥
        if parent not in self.dic:
            self.dic[parent] = parent

    # O(n) 返回老大哥
    def find(self, x):
        parent = self.dic[x]
        while parent != self.dic[parent]:
            parent = self.dic[parent]
        return parent

    # O(n) 合并老大哥，比如合并M和N家的二把手，先找到各自老大哥再合并这两个老大哥
    def union(self, master, branch):
        fa_master = self.find(master)
        fa_branch = self.find(branch)
        if fa_master != fa_branch:
            self.dic[fa_branch] = fa_master

test = Solution()
test.build('A', 'C')
test.build('B', 'C')
test.build('D', 'A')
test.build('F', 'E')
test.build('G', 'F')
print test.find('G')
test.union('D', 'G')
print test.find('G')
print test.dic