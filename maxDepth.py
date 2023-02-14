# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self,val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # bfs
    def maxDepth2(self, root):
        if not root:
            return 0
        res = 0
        queue = [root]
        while queue:
            for _ in range(len(queue)):
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res += 1
        return res

    # dfs
    def maxDepth(self, root):
        if root == None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        # print left, right
        return max(left, right) + 1

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
