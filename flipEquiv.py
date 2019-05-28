# -*- coding: utf-8 -*-
from sortedArrayToBST import Solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    def flipEquiv(self, root1, root2):
        stack1 = [root1]
        stack2 = [root2]
        while stack1 and stack2:
            curr1 = stack1.pop()
            curr2 = stack2.pop()
            #print curr1.val, curr2.val
            if curr1 and curr2:
                if curr1.val == curr2.val:
                    left1 = curr1.left
                    right1 = curr1.right
                    left2 = curr2.left
                    right2 = curr2.right
                    if left1.val == left2.val and right1.val == right2.val:
                        stack1 = stack1 + [left1] + [right1]
                        stack2 = stack2 + [left2] + [right2]
                    elif left1.val == right2.val and right1.val == left2.val:
                        stack1 = stack1 + [right1] + [left1]
                        stack2 = stack2 + [left2] + [right2]
                    else:
                        return False
                else:
                    return False
            elif not curr1 and not curr2:
                continue
            else:
                return False

        return True if not stack1 and not stack2 else False

test = Solution()
head_node1 = test.sortedArrayToBST([None, 2, None, 4, 5, 6, 7])
head_node2 = test.sortedArrayToBST([None, 2, None, 4, 5, 6, 7])
test1 = Solution1()
print test1.flipEquiv(head_node1, head_node2)

#    4
#  2   6
# 1 N 5 7