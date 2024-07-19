class Solution(object):
    def minimumArea(self, grid):
        top = float('inf')
        bottom = 0
        left = float('inf')
        right = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    top = min(top, i)
                    bottom = max(bottom, i)
                    left = min(left, j)
                    right = max(right, j)
        return (bottom - top + 1) * (right - left + 1)

test = Solution()
print test.minimumArea([[0,1,0],[1,0,1]])
print test.minimumArea([[1,0],[0,0]])