class Solution(object):
    def rotate(self, matrix):
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            return

        top = left = 0
        bottom = right = len(matrix) - 1
        n = len(matrix)

        # From outer to inner
        while n > 1:
            for i in range(n - 1):
                tmp = matrix[top][left + i]
                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = tmp
            top += 1
            left += 1
            bottom -= 1
            right -= 1
            n -= 2

        return matrix

test = Solution()
print test.rotate([[ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]])