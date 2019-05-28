# -*- coding: utf-8 -*-
from sortedArrayToBST import Solution
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def findMax(self, root, prev):
        if not root:
            return prev
        prev = root
        root = root.right
        return self.findMax(root, prev)

    def findMin(self, root, prev):
        if not root:
            return prev
        prev = root
        root = root.left
        return self.findMin(root, prev)

test = Solution()
head_node = test.sortedArrayToBST([0, 1, 2, 3, 4, 5, 6, 7])
test1 = Solution1()
print test1.findMax(head_node, None).val


#     4
#   2   6
#  1 3 5 7
# 0