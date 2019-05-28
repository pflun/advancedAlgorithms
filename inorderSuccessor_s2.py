from sortedArrayToBST import Solution

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def inorderSuccessor(self, root, p):
        self.prev = None
        self.res = None

        def compare(root):
            if root is None:
                return None

            if root.val == p:
                self.res = root
            elif root.val < p:
                compare(root.right)
            elif root.val > p:
                compare(root.right)

        compare(root)

        if self.res.right:
            return self.res.right.val
        else:
            return None

test = Solution()
head_node = test.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7])
test1 = Solution1()
print test1.inorderSuccessor(head_node, 6)

#    4
#  2   6
# 1 3 5 7