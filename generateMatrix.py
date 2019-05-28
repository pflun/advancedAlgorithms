# -*- coding: utf-8 -*-
# similar to LC54 spiralOrder.py
class Solution(object):
    def generateMatrix(self, n):
        if n <= 0:
            return []
        matrix = []
        counter = 1
        for i in range(n):
            tmp = []
            for j in range(n):
                tmp.append(0)
            matrix.append(tmp)

        rowStart = 0
        rowEnd = len(matrix) - 1
        colStart = 0
        colEnd = len(matrix[0]) - 1

        while rowStart <= rowEnd and colStart <= colEnd:
            # top
            for i in range(colStart, colEnd + 1):
                matrix[rowStart][i] = counter
                counter += 1
            rowStart += 1
            # right
            for i in range(rowStart, rowEnd + 1):
                matrix[i][colEnd] = counter
                counter += 1
            colEnd -= 1
            # bottom
            if rowStart <= rowEnd:
                for i in range(colEnd, colStart - 1, -1):
                    matrix[rowEnd][i] = counter
                    counter += 1
            rowEnd -= 1
            # left
            if colStart <= colEnd:
                for i in range(rowEnd, rowStart - 1, -1):
                    matrix[i][colStart] = counter
                    counter += 1
            colStart += 1

        return matrix

test = Solution()
print test.generateMatrix(4)