# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=9ZNky1wqNUw
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def _maxPathSum(self, root):
        if not root:
            return float('-inf')     # 0也行
        # 左右为负，宁愿不加
        l = max(0, self._maxPathSum(root.left))
        r = max(0, self._maxPathSum(root.right))
        # 保存当前左中右的最大值，但是返回给上层的时候左右只能返回一个
        self.ans = max(self.ans, root.val + l + r)
        return root.val + max(l, r)

    def maxPathSum(self, root):
        # 实例变量
        self.ans = float('-inf')
        self._maxPathSum(root)
        return self.ans

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

test = Solution()
print test.maxPathSum(head_node)

#     0
#   1   2
#  3 4
# 5
#  6