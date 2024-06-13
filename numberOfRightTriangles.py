class Solution(object):
    def numberOfRightTriangles(self, grid):
        res = 0
        row = [0 for _ in range(len(grid[0]))]
        col = [0 for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    row[j] += 1
                    col[i] += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res += (row[j] - 1) * (col[i] - 1)
        return res

test = Solution()
print test.numberOfRightTriangles([[0,1,0],[0,1,1],[0,1,0]])
print test.numberOfRightTriangles([[1,0,0,0],[0,1,0,1],[1,0,0,0]])
print test.numberOfRightTriangles([[1,0,1],[1,0,0],[1,0,0]])
print test.numberOfRightTriangles([[1,0,1]])
print test.numberOfRightTriangles([[1],[0],[1]])