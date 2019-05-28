# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums:
            return None

        mid = len(nums) / 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root


test = Solution()
# print test.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7, 10, 12, 24, 125]).val
# print test.sortedArrayToBST(['A', 'C', 'E', 'Y', 'P']).right.left.val