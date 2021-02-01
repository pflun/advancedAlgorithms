class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder[-1])
        inorderIndex = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[:inorderIndex], postorder[:inorderIndex])
        root.right = self.buildTree(inorder[inorderIndex + 1:], postorder[inorderIndex:-1])

        return root