class Solution(object):
    def satisfiesConditions(self, grid):
        for j in range(len(grid[0])):
            curr = grid[0][j]
            for i in range(1, len(grid)):
                if grid[i][j] != curr:
                    return False

        for i in range(1, len(grid[0])):
            if grid[0][i] == grid[0][i - 1]:
                return False

        return True