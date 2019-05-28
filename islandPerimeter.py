class Solution(object):
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