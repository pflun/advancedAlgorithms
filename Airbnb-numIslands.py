# -*- coding: utf-8 -*-
# You are playing a board game
# “G1, G2, W0, W1, S1”,
# “G2, G3, W0, W1, S1”,
# “S2, S3, S1, G1, S1”,
# “G1, G2, W0, W1, S1”,
# “G1, G2, W0, W1, S1”
# First character is the area type, second character is how many crowns are in that cell, the score is calculated as (area cell number) * (total number of the crowns in that area),
# Calculate the total score,
# Need to self write test cases
#
# For first area, G from (0, 0), the area score is (4 * 8)
# Second area W from (0, 2), the area score is (4 * 2)
# Return total score.

class Solution(object):
    def numIslands(self, grid):
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] is not None:
                    self.cells = 0
                    self.crowns = 0
                    self.dfs(grid, i, j, grid[i][j][0])
                    res += self.cells * self.crowns
        return res

    def dfs(self, grid, i, j, type):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] is None or grid[i][j][0] != type:
            return
        self.crowns += int(grid[i][j][1:])
        self.cells += 1
        grid[i][j] = None
        self.dfs(grid, i + 1, j, type)
        self.dfs(grid, i - 1, j, type)
        self.dfs(grid, i, j + 1, type)
        self.dfs(grid, i, j - 1, type)

test = Solution()
print test.numIslands(
    [['G1', 'G2', 'W0', 'W1', 'S1'],
    ['G2', 'G3', 'W0', 'W1', 'S1'],
    ['S2', 'S3', 'S1', 'G1', 'S1'],
    ['G1', 'G2', 'W0', 'W1', 'S1'],
    ['G1', 'G2', 'W0', 'W1', 'S1']]
)