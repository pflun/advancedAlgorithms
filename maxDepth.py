# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self,val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        if root == None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        # print left, right
        return max(left, right) + 1

    def pre_order(self, tree):
        if tree == None:
            return
        print tree.val
        self.pre_order(tree.left)
        self.pre_order(tree.right)

class Solution2(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        stack = [(root, 1)]
        res = 0
        while stack:
            node, level = stack.pop()
            res = max(res, level)
            if node.right:
                stack.append((node.right, level + 1))
            if node.left:
                stack.append((node.left, level + 1))
        return res

tree = TreeNode('D',TreeNode('B',TreeNode('A'),TreeNode('C')),TreeNode('E', right = TreeNode('G',TreeNode('F'))))
test = Solution2()
print test.maxDepth(tree)
