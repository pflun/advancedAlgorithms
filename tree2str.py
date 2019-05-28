# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def tree2str(self, t):
        self.res = ''

        def preorder(root):
            if not root:
                return
            self.res += '(' + str(root.val)

            preorder(root.left)
            preorder(root.right)

            self.res += ')'

        preorder(t)

        # write another function to filter out empty () => Done

        return self.res

head_node = TreeNode(0)
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
head_node.left = n1
head_node.right = n2
n1.left = n3
n3.left = n6
n6.left = n5
n6.right = n7

test1 = Solution()
print test1.tree2str(head_node)

#     0
#   1   2
#  3
# 6
#5 7