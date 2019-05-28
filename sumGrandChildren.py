# -*- coding: utf-8 -*-
# binary tree里面如果当前节点是even value，sum + 所有grand children的value。 返回sum
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumGrandChildren(self, root):
        self.res = 0

        def helper(root, depth):
            if not root:
                return None
            if depth == 0:
                self.res += root.val
            if root.left:
                helper(root.left, depth - 1)
            if root.right:
                helper(root.right, depth - 1)

        queue = [root]
        while queue:
            curr = queue.pop()
            if curr.val % 2 == 0:
                helper(curr, 2)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        return self.res

head_node = TreeNode(0)
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
head_node.left = n1
head_node.right = n2
n1.right = n3
n1.left = n4
n4.left = n5
n5.right = n6

test1 = Solution()
print test1.sumGrandChildren(head_node)

#     0
#   1   2
#  4 3
# 5
#  6


