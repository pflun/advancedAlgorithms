# Use deque
from sortedArrayToBST import Solution

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def zigzagLevelOrder(self, root):
        res = []
        iszig = 1

        if root == None:
            return res

        from collections import deque
        d = deque()
        d.append(root)

        while d:
            level = []
            size = len(d)
            if iszig == 1:
                for i in range(size):
                    head = d.popleft()
                    level.append(head.val)
                    if head.left != None:
                        d.append(head.left)
                    if head.right != None:
                        d.append(head.right)
                iszig = -1
                res.append(level)
            elif iszig == -1:
                for i in range(size):
                    head = d.pop()
                    level.append(head.val)
                    if head.right != None:
                        d.appendleft(head.right)
                    if head.left != None:
                        d.appendleft(head.left)
                iszig = 1
                res.append(level)

        return res

test = Solution()
head_node = test.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7])
test1 = Solution1()
print test1.zigzagLevelOrder(head_node)

#    4
#  2   6
# 1 3 5 7