# -*- coding: utf-8 -*-
# 两个node重合，是说他们在同一排，而且，在同一列。这道题和vertical order traversal类似。
#           Node1
#        /        \
#     Node2       Node3
#     /    \     /     \
# Node4   Node5, 6      Node7
#
# 这个tree 就有node重合，（Node5和Node6）
# return True: No coincide, False: has coincide
from sortedArrayToBST import Solution

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def coincideTreenode(self, root):

        if root == None:
            return False

        queue = []
        queue.append([0, root])

        # BFS, levelOrderTraversal
        while queue:
            dic = {}
            size = len(queue)
            for i in range(size):
                offset, head = queue.pop(0)
                # or use set()
                if offset in dic:
                    return False
                else:
                    dic[offset] = head

                if head.left != None:
                    queue.append([offset - 1, head.left])
                if head.right != None:
                    queue.append([offset + 1, head.right])

        return True


test = Solution()
head_node = test.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7])
test1 = Solution1()
print test1.coincideTreenode(head_node)

#    4
#  2   6
# 1 3 5 7