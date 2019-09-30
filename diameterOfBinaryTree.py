# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def diameterOfBinaryTree2(self, root):
        if not root:
            return 0
        self.res = 0

        def helper(node):
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            self.res = max(self.res, left + right + 1)
            return max(left, right) + 1

        helper(root)
        return self.res - 1

    def diameterOfBinaryTree(self, root):
        if not root or not root.left and not root.right:
            return 0
        res = 0
        stack = [root]

        while stack:
            curr = stack.pop(0)

            # 计算右子树最大深度
            right = self.helper(curr.right)
            # preorder
            if curr.right:
                stack.append(curr.right)

            left = self.helper(curr.left)
            if curr.left:
                stack.append(curr.left)

            # 左子树最大深度 ＋ 右子树最大深度
            res = max(res, left + right)

        return res

    # Get max depth
    def helper(self, root):
        # 到底返回0
        if not root:
            return 0

        left = self.helper(root.left) + 1
        right = self.helper(root.right) + 1

        # 最大深度是或左或右的最大值
        return max(left, right)

head_node = TreeNode(0)
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
head_node.left = n1
head_node.right = n2
n1.left = n3
n1.right = n4
n3.left = n6
n6.left = n5
n6.right = n7

test1 = Solution()
print test1.diameterOfBinaryTree(head_node)

#     0
#   1   2
#  3 4
# 6
#5 7