# -*- coding: utf-8 -*-
# 有个index bug
class Solution(object):
    def maximalRectangle(self, matrix):
        preprocess = []
        for i in range(len(matrix)):
            row = []
            for j in range(len(matrix[0])):
                tmp = (i + 1) * (j + 1)
                row.append(tmp)
            preprocess.append(row)

        maxArea = 0
        for i in range(len(matrix)):
            for j in range(0, i):
                for x in range(len(matrix[0])):
                    for y in (0, x):
                        if self.isValid(matrix, i, j, x, y):
                            currArea = preprocess[i][x] - preprocess[j][x] - preprocess[i][y] + preprocess[j][y]
                            maxArea = max(maxArea, currArea)

        return maxArea

    def isValid(self, matrix, i, j, x, y):
        for k in range(j, i):
            for z in range(y, x):
                if matrix[k][z] != '1':
                    return False
        return True

test = Solution()
print test.maximalRectangle([
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
])