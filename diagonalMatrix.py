# -*- coding: utf-8 -*-
# 比如
# 1 2 3.
# 4 5 6
# 7 8 9
#
# 就把 [7 5 3]打出来就行了
#
# 不过有可能不是square matrix就是了

class Solution(object):
    def diagonalMatrix(self, matrix):
        m = 0
        n = len(matrix) - 1
        res = []

        while m <= len(matrix[0]) - 1 and n >= 0:
            res.append(matrix[n][m])
            m += 1
            n -= 1

        return res


test = Solution()
print test.diagonalMatrix([
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50],
    [51, 53, 60, 70]
])