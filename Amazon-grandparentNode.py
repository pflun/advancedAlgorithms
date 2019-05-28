# -*- coding: utf-8 -*-
# 让你找出所有leaves的 grandparents node。Follow Up:如果是找出所有node距离any leaf with distance k
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def grandparentNode(self, root, k):
        self.res = []

        def dfs(root, ancestors, k):
            if not root.left and not root.right and len(ancestors) >= k:
                self.res.append(ancestors[-k].val)

            ancestors.append(root)

            if root.left:
                dfs(root.left, ancestors[:], k)
            if root.right:
                dfs(root.right, ancestors[:], k)

        dfs(root, [], k)
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
n1.left = n3
n1.right = n4
n3.left = n5
n5.right = n6

test1 = Solution()
print test1.grandparentNode(head_node, 2)

#     0
#   1   2
#  3 4
# 5
#  6