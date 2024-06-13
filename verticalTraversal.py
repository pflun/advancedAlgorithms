# -*- coding: utf-8 -*-
import collections
from sortedArrayToBST import Solution
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    # preorder无法保证纵向顺序，所以level order存(node, offset)
    def verticalTraversal2(self, root):
        g = collections.defaultdict(list)
        queue = [(root, 0)]
        while queue:
            new = []
            d = collections.defaultdict(list)
            for node, s in queue:
                d[s].append(node.val)
                if node.left:  new += (node.left, s - 1),
                if node.right: new += (node.right, s + 1),
            for i in d: g[i].extend(sorted(d[i]))
            queue = new
        return [g[i] for i in sorted(g)]

    def verticalTraversal(self, root):
        res = []
        dic = {}
        offset = 0

        def preorder(root, offset, dic):
            if not root:
                return
            preorder(root.left, offset - 1, dic)
            if offset in dic:
                dic[offset].append(root.val)
            else:
                dic[offset] = [root.val]
            preorder(root.right, offset + 1, dic)

        preorder(root, offset, dic)

        for i in sorted(dic.keys()):
            res.append(dic[i])

        return res

test = Solution()
head_node = test.sortedArrayToBST([0, 1, 2, 4, 5, 3, 6, 7])
test1 = Solution1()
print test1.verticalTraversal2(head_node)

#     5
#   2   6
#  1 4 3 7
# 0