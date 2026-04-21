# Maximum Island Perimeter
# Same Facebook-largestIslandPerimeter.py
# Each land cell has up to four edges. An edge contributes to the island's perimeter
# if it is either adjacent to water or lies on the boundary of the matrix.
# Return the maximum perimeter among all islands in the grid. If there is no island, return 0.
class Solution(object):
    def maxPerimeter(self, grid):
        self.dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.perimeter = 0
                    self.dfs(grid, set(), i, j)
                    res = max(res, self.perimeter)
        return res

    def dfs(self, grid, visited, i, j):
        if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]) or (i, j) in visited or grid[i][j] != 1:
            return
        visited.add((i, j))
        cnt = 4
        for d in self.dir:
            x = i + d[0]
            y = j + d[1]
            if x < 0 or x == len(grid) or y < 0 or y == len(grid[0]):
                continue
            if grid[x][y] == 1:
                cnt -= 1
            self.dfs(grid, visited, x, y)
        self.perimeter += cnt

test = Solution()
print test.maxPerimeter(
    [[1, 0, 1, 1, 1],
     [1, 0, 1, 1, 1],
     [0, 1, 0, 1, 1]])
print test.maxPerimeter(
    [[0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 1, 1, 1, 0],
     [0, 1, 0, 1, 1, 1, 0],
     [0, 0, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 0, 0]]
)
