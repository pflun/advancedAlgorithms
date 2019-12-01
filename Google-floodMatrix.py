# -*- coding: utf-8 -*-
# 一个N*N的沙盘（矩阵），每个格子有一个数字代表格子的高度， 沙盘左边有一条河，河的高度已知为H，求被淹没后的沙盘的样子（被淹没的地方的高度变成河的高度
class Solution(object):
    def floodMatrix(self, matrix, river):
        for i in range(len(matrix)):
            if matrix[i][0] < river:
                self.dfs(matrix, river, i, 0)
        return matrix

    def dfs(self, matrix, river, x, y):
        if x < 0 or x > len(matrix) - 1 or y < 0 or y > len(matrix[0]) - 1:
            return
        if matrix[x][y] < river:
            matrix[x][y] = river
            self.dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for d in self.dir:
                nx = x + d[0]
                ny = y + d[1]
                self.dfs(matrix, river, nx, ny)

test = Solution()
print test.floodMatrix([
  [1, 3, 5, 7],
  [10, 11, 16, 0],
  [23, 0, 34, 0],
  [51, 52, 54, 40]
], 11)