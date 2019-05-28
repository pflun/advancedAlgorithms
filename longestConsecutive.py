# 1
#  \
#   3
#  / \
# 2   4
#      \
#       5
# Longest consecutive sequence path is 3-4-5, so return 3.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def longestConsecutive(self, root):
        global res
        res = 0
        self.dfs(root, None, 0)
        return res


    def dfs(self, root, parent, length):
        global res

        if not root:
            return None

        if parent == None:
            length += 1
        elif root.val - parent.val == 1:
            length += 1
        else:
            length = 1

        res = max(res, length)

        self.dfs(root.left, root, length)
        self.dfs(root.right, root, length)

head_node = TreeNode(0)
n1 = TreeNode(1)
n2 = TreeNode(5)
n3 = TreeNode(2)
n4 = TreeNode(4)
n5 = TreeNode(3)
n6 = TreeNode(6)
head_node.left = n1
head_node.right = n2
n1.left = n3
n1.right = n4
n3.left = n5
n5.right = n6

test = Solution()
print test.longestConsecutive(head_node)

#     0
#   1   5
#  2 4
# 3
#  6