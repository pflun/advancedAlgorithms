# -*- coding: utf-8 -*-
# https://www.geeksforgeeks.org/print-the-matrix-diagonally-downwards/
# Given a matrix of size n*n, print the matrix in the following pattern.
# Examples:
# Input :matrix[2][2]= { {1, 2},
#                        {3, 4} }
# Output : 1 2 3 4
#
# Input :matrix[3][3]= { {1, 2, 3},
#                        {4, 5, 6},
#                        {7, 8, 9} }
# Output : 1 2 4 3 5 7 6 8 9
class Solution(object):
    def printDiagonally(self, matrix):
        cnt = 0
        res = []
        while cnt < len(matrix[0]) + len(matrix) - 1:
            for y in range(cnt + 1):
                x = cnt - y
                if x < len(matrix[0]) and y < len(matrix):
                    res.append(matrix[y][x])
            cnt += 1
        return res

test = Solution()
print test.printDiagonally([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])