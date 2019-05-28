# -*- coding: utf-8 -*-
# 有一个org chart，实现3个functions。setManager(a, b) : a is b's manager;
# setPeer(b, c) b and c work in same team as peers; query(a, b) whether a is under b's management.
class Solution(object):
    def __init__(self):
        self.dic = {}

    def setManager(self,a, b):
        if b not in self.dic:
            self.dic[b] = a
        else:
            return False

    def setPeer(self, b, c):
        if b in self.dic and c in self.dic:
            return False
        elif b in self.dic:
            self.dic[c] = self.dic[b]
        elif c in self.dic:
            self.dic[b] = self.dic[c]
        else:
            return False
        # corner case: if b is big boss such as Pichai, cannot set his peer

    def query(self,a, b):
        while a in self.dic:
            if self.dic[a] == b:
                return True
            a = self.dic[a]
        return False