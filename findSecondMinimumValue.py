# root is the smallest, so just traverse tree find node which is bigger than root but smaller than any other node
# early stop, don't have to traverse all nodes since parent is smaller than child
class Solution(object):
    def findSecondMinimumValue(self, root):
        self.res = float('inf')

        def dfs(node):
            if not node:
                return
            if root.val < node.val < self.res:
                self.res = node.val
                # early stop
                return
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return -1 if self.res == float('inf') else self.res