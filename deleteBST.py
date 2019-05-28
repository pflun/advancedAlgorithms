# -*- coding: utf-8 -*-
# 如果被删除节点有右子树，就把右子树的最小节点的值置换过来，删掉（跳过）最小节点
# 没有右子树的话，被删除节点的父节点直接指向（跳过）左子树
from sortedArrayToBST import Solution
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def deleteNode(self, root, key):
        if not root:
            return
        if not key:
            return root
        dummy = TreeNode(0)
        dummy.left = root
        p = root
        prev = dummy
        while p is not None and p.val != key:
            prev = p
            if p.val > key:
                p = p.left
            else:
                p = p.right
        if p is None:  # not found
            return root

        # has right subtree
        if p.right:
            minright = self.findMin(p.right, p, None)
            # exchange value between the min right child and deleted p
            p.val = minright.val
        else:
            # prev跳过p，删除p
            if prev.left == p:
                prev.left = p.left
            else:
                prev.right = p.left

        return dummy.left

    def findMin(self, root, prev, pprev):
        if not root:
            # 删除（跳过）最小节点，直接指向最小节点的右节点
            if pprev.left == prev:
                pprev.left = prev.right
            else:
                pprev.right = prev.right
            return prev
        pprev = prev
        prev = root
        root = root.left
        return self.findMin(root, prev, pprev)

test = Solution()
head_node = test.sortedArrayToBST([0, 1, 2, 3, 4, 5, 6, 7])
test1 = Solution1()
print test1.deleteNode(head_node, 4).right.right.val

#     4
#   2   6
#  1 3 5 7
# 0