from sortedArrayToBST import Solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    def main(self, root):
        res = self.preorderTraversal(root)

        return res

    def preorderTraversal(self, root):
        if root is None:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


test = Solution()
head_node = test.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7])
test1 = Solution1()
print test1.main(head_node)

#    4
#  2   6
# 1 3 5 7