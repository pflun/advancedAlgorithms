# -*- coding: utf-8 -*-
# 找preorder的下一节点
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderNext(self, root, target):
        self.res = None
        self.prev = None
        self.found = False

        def preorder(node, target):
            if not node:
                return
            if not self.found and self.prev == target:
                self.res = node
                self.found = True
                return

            self.prev = node.val
            preorder(node.left, target)
            preorder(node.right, target)

        preorder(root, target.val)
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

test = Solution()
print test.preorderNext(head_node, n5).val

#     0
#   1   2
#  3 4
# 5
#  6