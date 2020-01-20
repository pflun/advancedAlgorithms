# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def removeLeafNodes(self, root, target):

        def helper(node, prev, dir):
            if prev and dir:
                if not node.left and not node.right:
                    if node.val == target:
                        if dir == 'l':
                            prev.left = None
                            return 'deleted'
                        elif dir == 'r':
                            prev.right = None
                            return 'deleted'
            left = ''
            right = ''
            if node.left:
                left = helper(node.left, node, 'l')
            if node.right:
                right = helper(node.right, node, 'r')
            if left == 'deleted' and not node.right or right == 'deleted' and not node.left or left == 'deleted' and right == 'deleted':
                if node.val == target:
                    if dir == 'l':
                        prev.left = None
                        return 'deleted'
                    elif dir == 'r':
                        prev.right = None
                        return 'deleted'
            return

        helper(root, None, None)

        if not root.left and not root.right and root.val == target:
            return None

        return root

def preorder(node):
    if not node:
        return
    print node.val
    preorder(node.left)
    preorder(node.right)

head_node = TreeNode(2)
n1 = TreeNode(2)
n2 = TreeNode(2)
n3 = TreeNode(2)
n4 = TreeNode(2)
n5 = TreeNode(2)
n6 = TreeNode(2)
n7 = TreeNode(2)
head_node.left = n1
head_node.right = n2
n1.left = n3
n1.right = n4
n3.left = n5
n5.left = n6
n5.right = n7

test = Solution()
print preorder(test.removeLeafNodes(head_node, 2))

#     0
#   1   2
#  3 4
# 5
#6 7
