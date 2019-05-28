class Solution(object):
    def projectionArea(self, grid):
        m = len(grid)
        n = len(grid[0])

        top = 0
        side = 0
        for x in range(n):
            tmp = 0
            for y in range(m):
                # handle top
                if grid[y][x] != 0:
                    top += 1
                # get max col to handle side
                tmp = max(tmp, grid[y][x])
            side += tmp

        front = 0
        for g in grid:
            front += max(g)

        return front + side + top

test = Solution()
print test.projectionArea([[0],[0]])