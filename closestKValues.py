# inorder traverse to get a sorted list of treenode val, use heap to maintain k closest treenode val
# two pointers can reach O(n) time, see findClosestElements.py

import heapq
from sortedArrayToBST import Solution
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def closestKValues(self, root, target, k):
        res = []
        heap = []
        kres = []

        self.inorder(root, res)

        heapq.heapify(heap)
        for num in res:
            heapq.heappush(heap, [abs(num - target), num])

        for num in range(k):
            kres.append(heapq.heappop(heap)[1])

        return kres

    def inorder(self, root, res):
        if not root:
            return None

        if root.left:
            self.inorder(root.left, res)

        res.append(root.val)

        if root.right:
            self.inorder(root.right, res)

        return res



test = Solution()
head_node = test.sortedArrayToBST([1, 2, 3, 4, 6, 9, 20])
test1 = Solution1()
print test1.closestKValues(head_node, 2, 3)

#    4
#  2   9
# 1 3 6 20