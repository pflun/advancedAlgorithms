class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0

        l = len(grid)
        w = len(grid[0])
        h = 0

        for g in grid:
            tmpH = max(g)
            h = max(h, tmpH)

        print l, w, h
        return 2 * l * h + 2 * w * h + 2 * l * w

test = Solution()
print test.surfaceArea([[1,2],[3,4]])