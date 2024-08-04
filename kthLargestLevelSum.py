import heapq
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def kthLargestLevelSum(self, root, k):
        levelSum = []
        queue = [root]
        while queue:
            size = len(queue)
            tmp = 0
            for _ in range(size):
                curr = queue.pop(0)
                tmp += curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            levelSum.append(-tmp)
        if len(levelSum) < k:
            return -1
        heapq.heapify(levelSum)
        while levelSum and k > 1:
            heapq.heappop(levelSum)
            k -= 1
        return -heapq.heappop(levelSum)
