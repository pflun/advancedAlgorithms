from sortedArrayToBST import Solution

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def upsideDownBinaryTree(self, root):
        if root is None or root.left is None:
            return root

        newRoot = self.upsideDownBinaryTree(root.left)
        # first operation start at 2.left.left(4.left) = 5, 4.left = 2
        root.left.left = root.right
        root.left.right = root
        root.left = None
        root.right = None
        return newRoot

# This problem is kinda like reverse linkedlist
# http://bangbingsyb.blogspot.com/2014/11/leetcode-binary-tree-upside-down.html
#     1
#    / \
#   2   3
#  / \
# 4   5
#
#     4
#    / \
#   5   2
#      / \
#     3   1