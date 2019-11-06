# -*- coding: utf-8 -*-
# https://www.geeksforgeeks.org/merge-two-bsts-with-limited-extra-space/
# Given two Binary Search Trees(BST), print the elements of both BSTs in sorted
# form. The expected time complexity is O(m+n) where m is the number of nodes in
# first tree and n is the number of nodes in second tree. Maximum allowed
# auxiliary space is O(height of the first tree + height of the second tree).
#
# Examples:
#
# First BST
#        3
#     /     \
#    1       5
# Second BST
#     4
#   /   \
# 2       6
# Output: 1 2 3 4 5 6
#
#
# First BST
#           8
#          / \
#         2   10
#        /
#       1
# Second BST
#           5
#          /
#         3
#        /
#       0
# Output: 0 1 2 3 5 8 10
from sortedArrayToBST import Solution
class Solution1(object):
    def __init__(self, root1, root2):
        self.res = []
        self.stack1 = []
        self.stack2 = []
        while root1:
            self.stack1.append(root1)
            root1 = root1.left
        while root2:
            self.stack2.append(root2)
            root2 = root2.left

    def merge(self):
        curr1 = self.next1()
        curr2 = self.next2()
        while len(self.stack1) > 0 and len(self.stack2) > 0:
            if curr1 <= curr2:
                self.res.append(curr1)
                curr1 = self.next1()
            else:
                self.res.append(curr2)
                curr2 = self.next2()
        while len(self.stack1) > 0:
            curr = self.next1()
            self.res.append(curr)
        while len(self.stack2) > 0:
            curr = self.next2()
            self.res.append(curr)
        return self.res

    # 每次pop栈先检查curr有没有右节点，把右节点入栈并且继续弹入右节点的所有左节点
    def next1(self):
        curr = self.stack1.pop()
        tmp = curr.right
        while tmp:
            self.stack1.append(tmp)
            tmp = tmp.left
        return curr.val

    def next2(self):
        curr = self.stack2.pop()
        tmp = curr.right
        while tmp:
            self.stack2.append(tmp)
            tmp = tmp.left
        return curr.val

testBST = Solution()
root1 = testBST.sortedArrayToBST([0, 1, 4, 5, 6, 8])
root2 = testBST.sortedArrayToBST([2, 3, 5, 7, 9, 10])
test = Solution1(root1, root2)
print test.merge()