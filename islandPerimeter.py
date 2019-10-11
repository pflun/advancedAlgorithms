class Solution(object):
    def islandPerimeter2(self, grid):
        if len(grid) == 0:
            return 0
        island = 0
        edge = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    island += 1
                    edge += self.neighbor(grid, i, j)
        return island * 4 - edge

    def neighbor(self, grid, i, j):
        cnt = 0
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for d in dir:
            x = i + d[0]
            y = j + d[1]
            if x < 0 or x == len(grid) or y < 0 or y == len(grid[0]):
                continue
            if grid[x][y] == 1:
                cnt += 1
        return cnt

    def islandPerimeter(self, grid):
        res = 0
        island = 0
        neighbor = 0

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1:
                    island += 1
                    # Check if down neighbor
                    if i < len(grid) - 1 and grid[i + 1][j] == 1:
                        neighbor += 1
                    # Check if right neighbor
                    if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
                        neighbor += 1

        # an island has 4 borders, a neighbor rm a pair (2) of border
        res = (island * 4) - (neighbor * 2)
        return res


test = Solution()
print test.islandPerimeter(
 [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]])