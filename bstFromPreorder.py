class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        if len(preorder) == 0:
            return None
        elif len(preorder) == 1:
            return TreeNode(preorder[0])
        curr = TreeNode(preorder[0])
        left = self.searchSmall2(preorder[1:], preorder[0])
        curr.left = self.bstFromPreorder(preorder[1:left + 2])
        curr.right = self.bstFromPreorder(preorder[left + 2:])

        return curr

    # liner
    def searchSmall2(self, arr, target):
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] < target:
                return i
        return -1

    # find the first element smaller than target, bug
    def searchSmall(self, arr, target):
        low = 0
        high = len(arr) - 1
        while low < high:
            mid = (low + high) / 2
            if arr[mid] >= target:
                high = mid - 1
            else:
                low = mid
        return high

test = Solution()
print test.bstFromPreorder([8,5,1,7,10,12]).left.right.val
print test.searchSmall([5,1,7,10,12], 8)