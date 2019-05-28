class Solution(object):
    def maxAreaOfIsland(self, grid):
        res = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    visited = set()
                    self.size = 0
                    self.dfs(grid, i, j, visited)
                    res = max(res, self.size)

        return res

    def dfs(self, grid, i, j, visited):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or (i, j) in visited or grid[i][j] != 1:
            return

        visited.add((i, j))
        self.size += 1
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for d in dir:
            currx = i + d[0]
            curry = j + d[1]
            self.dfs(grid, currx, curry, visited)

test = Solution()
print test.maxAreaOfIsland([
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]])
