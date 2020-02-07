# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxProduct(self, root):
        self.diff = float('inf')
        self.sum = 0
        self.stack = [root]

        # get sum
        while self.stack:
            curr = self.stack.pop()
            self.sum += curr.val
            if curr.right:
                self.stack.append(curr.right)
            if curr.left:
                self.stack.append(curr.left)

        def helper(node):
            if not node.left and not node.right:
                return node.val
            left = 0
            right = 0
            if node.left:
                left = helper(node.left)
            self.diff = min(self.diff, abs(left - (self.sum - left)))
            if node.right:
                right = helper(node.right)
            self.diff = min(self.diff, abs(right - (self.sum - right)))

            return left + node.val + right

        helper(root)
        return ((self.sum - self.diff) / 2) * ((self.sum - self.diff) / 2 + self.diff) % (10**9+7)

head_node = TreeNode(1)
n1 = TreeNode(2)
n2 = TreeNode(3)
n3 = TreeNode(4)
n4 = TreeNode(5)
n5 = TreeNode(6)
head_node.left = n1
head_node.right = n2
n1.left = n3
n1.right = n4
n2.left = n5
test1 = Solution()
print test1.maxProduct(head_node)

# head_node = TreeNode(0)
# n1 = TreeNode(1)
# n2 = TreeNode(2)
# n3 = TreeNode(3)
# n4 = TreeNode(4)
# n5 = TreeNode(5)
# n6 = TreeNode(6)
# n7 = TreeNode(7)
# n55 = TreeNode(5)
# n66 = TreeNode(6)
# n77 = TreeNode(7)
# head_node.left = n1
# head_node.right = n2
# n1.left = n3
# n1.right = n4
# n3.left = n6
# n6.left = n5
# n6.right = n7
# n2.right = n66
# n66.left = n55
# n66.right = n77
#
# test1 = Solution()
# print test1.maxProduct(head_node)

#     0
#   1   2
#  3 4   6
# 6     5 7
#5 7