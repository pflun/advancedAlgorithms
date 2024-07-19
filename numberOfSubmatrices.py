class Solution(object):
    def numberOfSubmatrices(self, grid):
        res = 0
        countX = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        countY = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        if grid[0][0] == 'X':
            countX[0][0] = 1
        elif grid[0][0] == 'Y':
            countY[0][0] = 1
        for i in range(1, len(grid)):
            if grid[i][0] == 'X':
                countX[i][0] = 1 + countX[i - 1][0]
                countY[i][0] = countY[i - 1][0]
            elif grid[i][0] == 'Y':
                countY[i][0] = 1 + countY[i - 1][0]
                countX[i][0] = countX[i - 1][0]
            elif grid[i][0] == '.':
                countX[i][0] = countX[i - 1][0]
                countY[i][0] = countY[i - 1][0]
        for j in range(1, len(grid[0])):
            if grid[0][j] == 'X':
                countX[0][j] = 1 + countX[0][j - 1]
                countY[0][j] = countY[0][j - 1]
            elif grid[0][j] == 'Y':
                countY[0][j] = 1 + countY[0][j - 1]
                countX[0][j] = countX[0][j - 1]
            elif grid[0][j] == '.':
                countX[0][j] = countX[0][j - 1]
                countY[0][j] = countY[0][j - 1]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                if grid[i][j] == 'X':
                    countX[i][j] = countX[i - 1][j] + countX[i][j - 1] - countX[i - 1][j - 1] + 1
                    countY[i][j] = countY[i - 1][j] + countY[i][j - 1] - countY[i - 1][j - 1]
                elif grid[i][j] == 'Y':
                    countY[i][j] = countY[i - 1][j] + countY[i][j - 1] - countY[i - 1][j - 1] + 1
                    countX[i][j] = countX[i - 1][j] + countX[i][j - 1] - countX[i - 1][j - 1]
                elif grid[i][j] == '.':
                    countX[i][j] = countX[i - 1][j] + countX[i][j - 1] - countX[i - 1][j - 1]
                    countY[i][j] = countY[i - 1][j] + countY[i][j - 1] - countY[i - 1][j - 1]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if countX[i][j] == countY[i][j] and countX[i][j] >= 1:
                    res += 1
        return res

test = Solution()
print test.numberOfSubmatrices([["X","Y","."],["Y",".","."]])
print test.numberOfSubmatrices([["X","X"],["X","Y"]])
print test.numberOfSubmatrices([[".","."],[".","."]])
