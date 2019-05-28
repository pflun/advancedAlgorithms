# -*- coding: utf-8 -*-
# 利用inorder的顺序，取出一个node就看看它有没有right child，以及right child有没有左child，入栈（因为入栈的就是next smallest）。stack里一直是降序
from sortedArrayToBST import Solution
# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.stack) > 0

    # @return an integer, the next smallest number
    def next(self):
        node = self.stack.pop()
        x = node.right
        while x:
            self.stack.append(x)
            x = x.left
        return node.val

testBST = Solution()
root = testBST.sortedArrayToBST([0, 1, 2, 3, 4, 5, 6, 7])
test = BSTIterator(root)
print test.next()
print test.next()
print test.next()
print test.next()
print test.next()
# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

#     4
#   2   6
#  1 3 5 7
# 0