# http://www.lintcode.com/zh-cn/problem/search-a-2d-matrix-ii/
class Solution:

    def searchMatrix(self, matrix, target):
        # write your code here
        if len(matrix) == 0 or not target:
            return 0

        counter = 0
        i = len(matrix) - 1
        j = 0

        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] == target:
                counter += 1
                i -= 1
            elif matrix[i][j] > target:
                i -= 1

            elif matrix[i][j] < target:
                j += 1

        return counter