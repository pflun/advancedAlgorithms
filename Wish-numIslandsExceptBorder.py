# -*- coding: utf-8 -*-
# 边缘的岛不算的话有几个，加一个bool找到边界就set true，如果true counter就不加。然后bool set回false
class Solution(object):
    def numIslands(self, grid):
        self.res = 0
        self.dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        self.border = False
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    if not self.boarder:
                        self.res += 1
                    self.boarder = False
        return self.res, grid

    def dfs(self, grid, i, j):
        if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1 or grid[i][j] != '1':
            return
        if i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1:
            self.boarder = True
        grid[i][j] = '2'
        for d in self.dir:
            y = d[0] + i
            x = d[1] + j
            self.dfs(grid, y, x)

test = Solution()
print test.numIslands([
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","0","1","0","0"],
    ["0","0","0","0","0"]])