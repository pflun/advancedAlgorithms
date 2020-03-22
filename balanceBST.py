# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from treeDesirializer import deserialize

class Solution(object):
    def balanceBST(self, root):
        nums = []
        res = self.inorder(root, nums)
        return self.sortedArrayToBST(res)

    def inorder(self, root, res):
        if not root:
            return None
        if root.left:
            self.inorder(root.left, res)
        res.append(root.val)
        if root.right:
            self.inorder(root.right, res)

        return res

    def sortedArrayToBST(self, nums):
        if not nums:
            return None

        mid = len(nums) / 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root

head = deserialize('[1,null,2,null,3,null,4,null,null]')
head2 = deserialize('[14,9,16,2,13]')
test = Solution()
print test.balanceBST(head2)