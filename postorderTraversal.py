# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        res = []

        def postorder(root, res):
            if root is None:
                return None
            postorder(root.left, res)
            postorder(root.right, res)
            res.append(root.val)

        postorder(root, res)

        return res

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
print test.postorderTraversal(head_node)

#     0
#   1   2
#  3 4
# 5
#  6