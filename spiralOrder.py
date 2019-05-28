# -*- coding: utf-8 -*-
# 特别注意处理 “下” 和 “左” 边界的时候，有可能当前这层只有一行，或者一列，已经输出过了不需要重复输出。所以这两条边的循环上要注意加一个判断条件。
class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        res = []

        rowStart = 0
        rowEnd = len(matrix) - 1
        colStart = 0
        colEnd = len(matrix[0]) - 1

        while rowStart <= rowEnd and colStart <= colEnd:
            # top
            for i in range(colStart, colEnd + 1):
                res.append(matrix[rowStart][i])
            rowStart += 1
            # right
            for i in range(rowStart, rowEnd + 1):
                res.append(matrix[i][colEnd])
            colEnd -= 1
            # bottom
            if rowStart <= rowEnd:
                for i in range(colEnd, colStart - 1, -1):
                    res.append(matrix[rowEnd][i])
            rowEnd -= 1
            # left
            if colStart <= colEnd:
                for i in range(rowEnd, rowStart - 1, -1):
                    res.append(matrix[i][colStart])
            colStart += 1

        return res

test = Solution()
print test.spiralOrder([
  [1, 3, 5, 7],
  [10, 11, 16, 0],
  [23, 0, 34, 0],
  [51, 52, 54, 40]
])