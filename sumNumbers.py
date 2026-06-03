from sortedArrayToBST import Solution

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def sumNumbers(self, root):
        if root is None:
            return []
        stack = [(root, root.val)]
        res = 0

        while stack:
            node, value = stack.pop()
            if not node.left and not node.right:
                res += value
            if node.right:
                stack.append((node.right, value * 10 + node.right.val))
            if node.left:
                stack.append((node.left, value * 10 + node.left.val))

        return res

    def sumNumbers2(self, root):
        res = []

        def dfs(node, prev):
            if not node.left and not node.right:
                res.append(prev * 10 + node.val)
            if node.left:
                dfs(node.left, prev * 10 + node.val)
            if node.right:
                dfs(node.right, prev * 10 + node.val)

        dfs(root, 0)
        return sum(res)

test = Solution()
head_node = test.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7])
test1 = Solution1()
print test1.sumNumbers(head_node)

#    4
#  2   6
# 1 3 5 7