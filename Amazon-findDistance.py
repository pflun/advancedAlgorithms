# -*- coding: utf-8 -*-
# Given a list of unique integers, construct the binary tree by given order without rebalancing,
# then find out the distance between two nodes
# construct BST ==> sortedArrayToBST.py
# 这道题如果改成binary tree而不是BST，用lowestCommonAncestor.py

from sortedArrayToBST import Solution
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def findDistance(self, root, p, q):
        # 最小公共祖先
        parent = self.lowestCommonAncestor(root, p, q)
        # 分别算从LCA到 p q 需要多少步
        self.resP = self.lcaToNode(parent, p, 0)
        self.resQ = self.lcaToNode(parent, q, 0)

        return self.resP + self.resQ

    def lcaToNode(self, parent, node, res):
        if not parent:
            return None
        # found
        if parent == node:
            return res
        left = self.lcaToNode(parent.left, node, res + 1)
        right = self.lcaToNode(parent.right, node, res + 1)
        if left:
            return left
        elif right:
            return right


    def lowestCommonAncestor(self, root, p, q):
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
head_node = test.sortedArrayToBST([0, 1, 2, 3, 4, 5, 6, 7])
p = head_node.left.left.left
q = head_node.right.right
test1 = Solution1()
print test1.findDistance(head_node, p, q)
# print test1.lcaToNode(head_node, q, 0)

#     4
#   2   6
#  1 3 5 7
# 0