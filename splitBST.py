# -*- coding: utf-8 -*-
from sortedArrayToBST import Solution
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 此外 It's not necessarily the case that the tree contains a node with value V。 多写几个if判断 V 在 root与prev之间
class Solution1:
    def splitBST(self, root, V):
        self.root = root
        self.V = None

        def helper(root, V, prev):
            if not root:
                return
            if root.val == V:
                if prev.left == root:
                    self.V = root
                    prev.left = root.right
                elif prev.right == root:
                    self.V = root.right
                    root.right = None

            if root.val > V:
                helper(root.left, V, root)
            elif root.val < V:
                helper(root.right, V, root)

        helper(root, V, None)

        return [self.root.val, self.V.val]

test = Solution()
head_node = test.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7])
test1 = Solution1()
print test1.splitBST(head_node, 6)

#    4
#  2   6
# 1 3 5 7
