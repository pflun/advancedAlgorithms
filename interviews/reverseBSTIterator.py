# Imagine you're given a very large binary search tree, which cannot fit entire tree into the memory
# So you're asked to implement a PREV iterator with two APIs, hasPrev() and prev()
# hasPrev() returns whether a previous number exist, prev() returns the previous largest number
from sortedArrayToBST import Solution
# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTPrevIterator(object):
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.right

    # @return a boolean, whether a previous number exist
    def hasPrev(self):
        return len(self.stack) > 0

    # @return an integer, the previous largest number
    def prev(self):
        node = self.stack.pop()
        x = node.left
        while x:
            self.stack.append(x)
            x = x.right
        return node.val

testBST = Solution()
root = testBST.sortedArrayToBST([0, 1, 2, 3, 4, 5, 6, 7])
test = BSTPrevIterator(root)
print test.prev()
print test.prev()
print test.prev()
print test.prev()
print test.prev()

#     4
#   2   6
#  1 3 5 7
# 0