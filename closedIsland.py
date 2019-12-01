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

        return res, grid

test = Solution()
print test.closedIsland([[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]])