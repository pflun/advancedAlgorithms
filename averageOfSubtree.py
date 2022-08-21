# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        self.res = 0

        def helper(node):
            if not node:
                return 0, 0
            left_total, left_nums = helper(node.left)
            right_total, right_nums = helper(node.right)
            total_val = left_total + right_total + node.val
            total_nums = left_nums + right_nums + 1
            if node.val == total_val / total_nums:
                self.res += 1

            return total_val, total_nums
        helper(root)

        return self.res

head_node = TreeNode(4)
n1 = TreeNode(8)
n2 = TreeNode(5)
n3 = TreeNode(0)
n4 = TreeNode(1)
n5 = TreeNode(6)
head_node.left = n1
head_node.right = n2
n1.left = n3
n1.right = n4
n2.right = n5
test1 = Solution()
print test1.averageOfSubtree(head_node)