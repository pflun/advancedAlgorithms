from sortedArrayToBST import Solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    def isValidBST(self, root):
        res = self.inorderTraversal(root)

        for i in range(len(res) - 1):
            if res[i + 1] <= res[i]:
                return False

        return True

    def inorderTraversal(self, root):
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def isValidBST2(self, root):

        def inorder(root, res):
            if not root:
                return None

            if root.left:
                inorder(root.left, res)

            res.append(root.val)

            if root.right:
                inorder(root.right, res)

            return res

        arr = inorder(root, [])

        for i in range(len(arr) - 1):
            if arr[i + 1] <= arr[i]:
                return False

        return True


test = Solution()
head_node = test.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7])
test1 = Solution1()
print test1.isValidBST2(head_node)

#    4
#  2   6
# 1 3 5 7