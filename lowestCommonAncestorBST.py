# -*- coding: utf-8 -*-
from sortedArrayToBST import Solution

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# lowest common ancestor in BST is a node that smaller(equal) than one node AND larger(equal) than the other node, 6 is the LCA of 5 and 7
class Solution1(object):
    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return root

        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)

        return root

    def lowestCommonAncestor2(self, root, p, q):
        minval = min(p.val, q.val)
        maxval = max(p.val, q.val)

        while root:
            # case 6, 7, return 6
            if root.val == minval:
                return root
            # case 5, 6, return 6
            elif root.val == maxval:
                return root
            # case 5, 7, return 6
            elif root.val < maxval and root.val > minval:
                return root
            # p q 同时在右侧
            elif root.val < minval:
                root = root.right
            # p q 同时在左侧
            elif root.val > maxval:
                root = root.left


test = Solution()
head_node = test.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7])
n2 = head_node.left
n5 = head_node.right.left
n6 = head_node.right
n7 = head_node.right.right
test1 = Solution1()
print test1.lowestCommonAncestor2(head_node, n2, n7).val

#    4
#  2   6
# 1 3 5 7