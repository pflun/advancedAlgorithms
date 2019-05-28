# -*- coding: utf-8 -*-
# 计算所有left child node的和
# Definition for a binary tree node.
from sortedArrayToBST import Solution

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def leftChildSum(self, root):
        if not root:
            return 0
        self.res = 0

        def dfs(root):
            if not root:
                return None
            if root.left:
                self.res += root.left.val
                dfs(root.left)
            if root.right:
                dfs(root.right)

        dfs(root)
        return self.res

test = Solution()
head_node = test.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7])
test1 = Solution1()
print test1.leftChildSum(head_node)

#    4
#  2   6
# 1 3 5 7
