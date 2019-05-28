# -*- coding: utf-8 -*-
# postorder traversal: https://mnmunknown.gitbooks.io/algorithm-notes/content/post_order_traversal_de_ying_yong.html
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestorDeepestLeaf(self, root):
        self.curLCA = None
        self.maxDepth = 0

        def postOrder(root, depth):
            # Edge/Condition
            if not root:
                return 0
            if not root.left and not root.right:
                if depth > self.maxDepth:
                    self.curLCA = root
                    self.maxDepth = depth
                return depth

            # Divide
            left = postOrder(root.left, depth + 1)
            right = postOrder(root.right, depth + 1)

            # Conquer
            #
            if left == right and left >= self.maxDepth:
                self.maxDepth = max(left, self.maxDepth)
                self.curLCA = root

            return max(left, right)

        postOrder(root, 0)

        return self.curLCA


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
n3.left = n5
n5.left = n6
n5.right = n7

test1 = Solution()
print test1.lowestCommonAncestorDeepestLeaf(head_node).val

#     0
#   1   2
#  3 4
# 5
#6 7