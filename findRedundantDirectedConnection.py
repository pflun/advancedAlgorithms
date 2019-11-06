# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=lnmJT5b4NlM
# 三种情况，两种重复顶点分别处理，一种找环
class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        children = set()
        # step 1, check if multiple parents
        for e in edges:
            if e[1] in children:
                return False
            else:
                children.add(e[1])

        # step 2, apply Union Find to find circle
        