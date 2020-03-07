class Solution(object):
    def countNegatives(self, grid):
        res = 0
        i = len(grid) - 1
        j = 0
        while i >= 0 and j < len(grid[0]):
            if grid[i][j] < 0:
                res += len(grid[0]) - j
                i -= 1
            else:
                j += 1
        return res

test = Solution()
print test.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])
print test.countNegatives([[3,2],[1,0]])
print test.countNegatives([[1,-1],[-1,-1]])
print test.countNegatives([[-1]])