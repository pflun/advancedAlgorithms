# Bottom up so that once done with children, delete the node
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        self.to_delete = set(to_delete)
        self.res = [] if root.val in self.to_delete else [root]

        def helper(node):
            if not node:
                return
            if node.left:
                helper(node.left)
                if node.left.val in self.to_delete:
                    node.left = None
            if node.right:
                helper(node.right)
                if node.right.val in self.to_delete:
                    node.right = None
            left = node.left
            right = node.right
            if node.val in self.to_delete:
                if left:
                    self.res.append(left)
                if right:
                    self.res.append(right)
                del node

        helper(root)
        return self.res

head_node = TreeNode(0)
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n55 = TreeNode(5)
n66 = TreeNode(6)
n77 = TreeNode(7)
head_node.left = n1
head_node.right = n2
n1.left = n3
n1.right = n4
n3.left = n6
n6.left = n5
n6.right = n7
n2.right = n66
n66.left = n55
n66.right = n77
#     0
#   1   2
#  3 4   6
# 6     5 7
#5 7
test = Solution()
print test.delNodes(head_node, [2])
