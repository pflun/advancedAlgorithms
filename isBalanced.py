# The algorithm can be optimized because if one of its sub tree is unbalanced, we can stop. In the height function, if abs( height of left - height of right)>1, just raise Exception and catch it in the isBalanced.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def height(self, root):
        if not root: return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        if abs(self.height(root.left) - self.height(root.right)) > 1: return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    # Just for testing
    def sortedArrayToBST(self, nums):
        if not nums:
            return None

        mid = len(nums) / 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root


test = Solution()
print test.isBalanced(test.sortedArrayToBST([1, 2, 3, 5, 8, 10]))