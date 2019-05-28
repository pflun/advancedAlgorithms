# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self,val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if root.left==None or root.right==None:
            # either left + 1 or right + 1
            return left + right + 1
        return min(left, right) + 1

class Solution2(object):
    def minDepth(self, root):
        if root is None:
            return 0
        stack = [(root, 1)]
        res = float('inf')
        while stack:
            node, level = stack.pop()
            if not node.right and not node.left:
                res = min(res, level)
                # res = max(res, level)
            if node.right:
                stack.append((node.right, level + 1))
            if node.left:
                stack.append((node.left, level + 1))
        return res

tree = TreeNode('D',TreeNode('B',TreeNode('A'),TreeNode('C')),TreeNode('E', right = TreeNode('G',TreeNode('F'))))
test = Solution2()
print test.minDepth(tree)