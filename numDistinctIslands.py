# -*- coding: utf-8 -*-
class Solution(object):
    def numDistinctIslands(self, grid):
        if not grid:
            return 0

        shapes = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    shape = set()
                    # 以最先为1的位置为基点(i0, j0)，计算偏移量
                    self.dfs(grid, i, j, i, j, shape)
                    # 每次找到一个shape就加入shapes
                    if shape:
                        shapes.append(shape)

        # calculate how many duplicates, need to divide by 2
        counter = 0
        for i in range(len(shapes)):
            for j in range(len(shapes)):
                if i == j:
                    continue
                if shapes[i] == shapes[j]:
                    counter += 1

        return len(shapes) - (counter / 2)

    def dfs(self, grid, i, j, i0, j0, shape):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
            return
        # Set to 2 means visited
        grid[i][j] = 2
        # 当前点减去偏移量,加入shape
        shape.add((i - i0, j - j0))
        self.dfs(grid, i + 1, j, i0, j0, shape)
        self.dfs(grid, i - 1, j, i0, j0, shape)
        self.dfs(grid, i, j + 1, i0, j0, shape)
        self.dfs(grid, i, j - 1, i0, j0, shape)

test = Solution()
print test.numDistinctIslands(
 [[1, 1, 0, 0, 0],
  [0, 1, 0, 0, 1],
  [0, 0, 0, 1, 1],
  [0, 0, 0, 0, 0],
  [1, 1, 0, 1, 1]])
