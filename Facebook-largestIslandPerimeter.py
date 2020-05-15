# optimization: change 1 to 2 after visit and get rid off visited set
class Solution(object):
    def largestIslandPerimeter(self, grid):
        self.dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    visited = set()
                    self.perimeter = 0
                    self.dfs(grid, i, j, visited)
                    res = max(res, self.perimeter)

        return res

    def dfs(self, grid, i, j, visited):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or (i, j) in visited or grid[i][j] != 1:
            return

        visited.add((i, j))
        # calculate boarder for each cell
        cnt = 4
        for d in self.dir:
            x = i + d[0]
            y = j + d[1]
            if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and grid[x][y] == 1:
                cnt -= 1
        self.perimeter += cnt

        for d in self.dir:
            currx = i + d[0]
            curry = j + d[1]
            self.dfs(grid, currx, curry, visited)

test = Solution()
print test.largestIslandPerimeter(
    [[1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 1, 1]])
print test.largestIslandPerimeter(
[[0, 0, 0, 0, 0, 0, 0],
 [0, 1, 0, 1, 1, 1, 0],
 [0, 1, 0, 1, 1, 1, 0],
 [0, 0, 1, 1, 1, 1, 0],
 [0, 0, 0, 0, 0, 0, 0]]
)