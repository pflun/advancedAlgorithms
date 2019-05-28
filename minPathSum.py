# -*- coding: utf-8 -*-
# Matrix DP, curr[i][j] is from its either left or top
class Solution(object):
    def minPathSum(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j > 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0 and i > 0:
                    grid[i][j] += grid[i - 1][j]
                elif i > 0 and j > 0:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[len(grid) - 1][len(grid[0]) - 1]

    def minPathSum2(self, grid):
        matrix = []
        for i in range(len(grid)):
            tmp = []
            for j in range(len(grid[0])):
                tmp.append(0)
            matrix.append(tmp)

        matrix[0][0] = grid[0][0]
        for i in range(1, len(grid)):
            matrix[i][0] = matrix[i - 1][0] + grid[i][0]
        for j in range(1, len(grid[0])):
            matrix[0][j] = matrix[0][j - 1] + grid[0][j]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1]) + grid[i][j]

        return matrix[-1][-1]

    # Follow up 1：要求重建从end 到 start的路径
    # 用另一个额外数组记录每一步选择的parent，dp结束后，从end依次访问它的parent重建路径
    def minPathSum3(self, grid):
        matrix = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
        path = [] #这个path写错了，要记录当前是哪一点和之前一步是哪一点；最后从[-1][-1]倒着找

        matrix[0][0] = grid[0][0]
        for i in range(1, len(grid)):
            matrix[i][0] = matrix[i - 1][0] + grid[i][0]
        for j in range(1, len(grid[0])):
            matrix[0][j] = matrix[0][j - 1] + grid[0][j]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                if matrix[i - 1][j] >= matrix[i][j - 1]:
                    path.append([i, j - 1])
                    matrix[i][j] = matrix[i][j - 1] + grid[i][j]
                else:
                    path.append([i - 1, j])
                    matrix[i][j] = matrix[i - 1][j] + grid[i][j]

        return path

test = Solution()
print test.minPathSum2(
    [[1,3,1],
     [1,5,1],
     [4,2,1]])
print test.minPathSum3(
    [[1,3,1],
     [1,5,1],
     [4,2,1]])