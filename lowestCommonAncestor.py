# -*- coding: utf-8 -*-
# Time:  O(n)
# Space: O(1)
#
# Given a binary tree, find the lowest common ancestor (LCA)
# of two given nodes in the tree.
#
# According to the definition of LCA on Wikipedia: “The lowest
# common ancestor is defined between two nodes v and w as the
# lowest node in T that has both v and w as descendants (where we
# allow a node to be a descendant of itself).”
#
#         _______3______
#       /              \
#     ___5__          ___1__
#   /      \        /      \
#   6      _2       0       8
#          /  \
#          7   4
# For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3.
# Another example is LCA of nodes 5 and 4 is 5, since a node can be a
# descendant of itself according to the LCA definition.
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        # Edge/Condition
        if not root:
            return None
        if root == p or root == q:
            return root

        # Divide
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # Conquer
        # if found both 5 and 1, return 3
        if left and right:
            return root
        # case: 1 and 8, not left so return 8, then in previous recursion return 1 (if root == p or root == q: return root)
        if not left:
            return right
        if not right:
            return left

head_node = TreeNode(0)
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
head_node.left = n1
head_node.right = n2
n1.left = n3
n1.right = n4
n3.left = n5
n5.right = n6

test1 = Solution()
print test1.lowestCommonAncestor(head_node, n3, n2).val

#     0
#   1   2
#  3 4
# 5
#  6