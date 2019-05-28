# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        self.res = []

        def dfs(root, sum, ls, subsum):
            if not root or subsum > sum:
                return
            ls.append(root.val)
            subsum += root.val
            if not root.left and not root.right:
                if subsum == sum:
                    self.res.append(ls)
            dfs(root.left, sum, ls[:], subsum)
            dfs(root.right, sum, ls[:], subsum)

        dfs(root, sum, [], 0)

        return self.res

head_node = TreeNode(0)
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n14 = TreeNode(14)
head_node.left = n1
head_node.right = n2
n2.right = n14
n1.left = n3
n1.right = n4
n3.left = n5
n5.left = n6
n5.right = n7

test = Solution()
print test.pathSum(head_node, 16)

#     0
#   1   2
#  3 4   14
# 5
#6 7
