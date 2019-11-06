# -*- coding: utf-8 -*-
# 把edges转化成tree，每个edge第一个point是第二个point的parent。
#
# 输入是
# {{'a','b'}, {'a','d'}, {'b','c'}}
# 比如第一个：a是b的parent
#
# 最终转化成tree
#       a
#    b     d
#   c
# ANS:  先找到root，然后hashmap存，然后dfs/bfs
#
# (1)find root by set.
# set1: all_node
# set2: father
# (2)save edges into graph
# (3)BFS/DFS: convert graph into tree.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.children = []

class Solution(object):
    def edgesToTree(self, arr):
        graph = {}
        allSet = set()
        childrenSet = set()
        for a in arr:
            allSet.add(a[0])
            allSet.add(a[1])
            childrenSet.add(a[1])
        rootVal = ''
        for a in allSet:
            if a not in childrenSet:
                rootVal = a
        for a in arr:
            if a[0] not in graph:
                graph[a[0]] = [a[1]]
            else:
                graph.get(a[0]).append(a[1])
        root = TreeNode(rootVal)

        # dfs建多叉树
        def dfs(node, value):
            if value not in graph:
                return None
            for n in graph[value]:
                curr = TreeNode(n)
                node.children.append(curr)
                dfs(curr, n)
            return node

        dfs(root, rootVal)
        return root

test = Solution()
print test.edgesToTree([['a', 'b'], ['a', 'd'], ['b', 'c']])
