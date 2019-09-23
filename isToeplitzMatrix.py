class Solution(object):
    def isToeplitzMatrix(self, matrix):
        for j in range(len(matrix[0])):
            curr = matrix[0][j]
            for i in range(1, len(matrix)):
                if j + i < len(matrix[0]) and matrix[i][j + i] != curr:
                    return False
        for i in range(len(matrix)):
            curr = matrix[i][0]
            for j in range(1, len(matrix[0])):
                if i + j < len(matrix) and matrix[i + j][j] != curr:
                    return False
        return True