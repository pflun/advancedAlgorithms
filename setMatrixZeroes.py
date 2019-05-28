# -*- coding: utf-8 -*-
class Solution(object):
    def setZeroes(self, matrix):
        Zeros = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    Zeros.append([i, j])

        for k in range(len(Zeros)):
            for i in range(len(matrix)):
                matrix[i][Zeros[k][1]] = 0
            for j in range(len(matrix[0])):
                matrix[Zeros[k][0]][j] = 0


        return matrix

    def setZeroes2(self, matrix):
        if not matrix:
            return []

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][j] = '#'

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == '#':
                    matrix[i][j] = 0
                    for k in range(len(matrix[0])):
                        if matrix[i][k] != '#':
                            matrix[i][k] = 0
                    for v in range(len(matrix)):
                        if matrix[v][j] != '#':
                            matrix[v][j] = 0

        return matrix

test = Solution()
print test.setZeroes2([
  [1, 3, 5, 7],
  [10, 11, 16, 0],
  [23, 0, 34, 0],
  [51, 52, 54, 40]
])

# 将数组的0row和0column用来作为标志位记录他这一行或者一列是不是又0出现
# 但是之前要先检查0row和0column有没有为0的话  有的话就对一个布尔值置位
# 之后就先检查0row和0column的标志 然后根据标志来清零对应的行列
# 然后再根据布尔值来清零0row和0column