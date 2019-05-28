# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        self.mleft = 0
        self.mright = 0

        def helper(root, offset):
            if root.left:
                self.mleft = min(self.mleft, offset - 1)
                helper(root.left, offset - 1)
            if root.right:
                self.mright = max(self.mright, offset + 1)
                helper(root.right, offset + 1)

        helper(root, 0)

        return self.mright - self.mleft

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
print test1.widthOfBinaryTree(head_node)

#     0
#   1   2
#  3 4
# 6
#5 7