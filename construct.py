"""
# Definition for a QuadTree node.
"""
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

import numpy
class Solution(object):
    def construct(self, grid):
        root = self.helper(numpy.array(grid))
        return root

    def helper(self, grid):
        if len(grid) == 0:
            return None
        if self.isOnes(grid) == 1:
            return Node(True, True, None, None, None, None)
        elif self.isOnes(grid) == 0:
            return Node(False, True, None, None, None, None)
        else:
            midX = len(grid) / 2
            midY = len(grid) / 2
            topLeft = self.helper(grid[:midX, :midY])
            bottomLeft = self.helper(grid[midX:, :midY])
            topRight = self.helper(grid[:midX, midY:])
            bottomRight = self.helper(grid[midX:, midY:])
            return Node(False, None, topLeft, topRight, bottomLeft, bottomRight)

    def isOnes(self, grid):
        zero = None
        one = None
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    zero = True
                elif grid[i][j] == 1:
                    one = True
        if zero and one:
            return None
        elif zero:
            return 0
        elif one:
            return 1

test = Solution()
print test.construct([
    [1,1,1,1,0,0,0,0],
    [1,1,1,1,0,0,0,0],
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,0,0,0,0],
    [1,1,1,1,0,0,0,0],
    [1,1,1,1,0,0,0,0],
    [1,1,1,1,0,0,0,0]]).topRight.bottomRight.val