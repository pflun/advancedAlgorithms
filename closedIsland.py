# -*- coding: utf-8 -*-
class Solution(object):
    def closedIsland(self, grid):

        def dfs(grid, i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 0:
                return
            if i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[0]) - 1:
                self.boarder = True

            # Set to 2 means visited
            grid[i][j] = 2
            dfs(grid, i + 1, j)
            dfs(grid, i - 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i, j - 1)

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    self.boarder = False
                    dfs(grid, i, j)
                    if self.boarder == False:
                        res += 1

        return res

    # 先从border dfs所有land变成invalid，然后正常dfs border内land就行
    def closedIsland2(self, grid):
        self.dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        res = 0
        for j in range(len(grid[0])):
            if grid[0][j] == 0:
                self.invalid(grid, 0, j)
            if grid[-1][j] == 0:
                self.invalid(grid, len(grid) - 1, j)
        for i in range(len(grid)):
            if grid[i][0] == 0:
                self.invalid(grid, i, 0)
            if grid[i][-1] == 0:
                self.invalid(grid, i, len(grid[0]) - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    res += 1
                    self.dfs(grid, i, j)

        return res

    def invalid(self, grid, i, j):
        if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1 or grid[i][j] != 0:
            return
        grid[i][j] = 2
        for d in self.dir:
            x = i + d[0]
            y = j + d[1]
            self.invalid(grid, x, y)

    def dfs(self, grid, i, j):
        if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1 or grid[i][j] != 0:
            return
        grid[i][j] = 3
        for d in self.dir:
            x = i + d[0]
            y = j + d[1]
            self.invalid(grid, x, y)

test = Solution()
print test.closedIsland([[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]])