# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isEvenOddTree(self, root):
        queue = [root]
        isEven = False
        while queue:
            size = len(queue)
            prev = None
            if not isEven:
                isEven = True
            else:
                isEven = False
            for _ in range(size):
                curr = queue.pop(0)
                if isEven and curr.val % 2 == 0:
                    return False
                elif not isEven and curr.val % 2 != 0:
                    return False
                if isEven and prev and curr.val <= prev:
                    return False
                if not isEven and prev and curr.val >= prev:
                    return False
                prev = curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return True