class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or target is None:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        x = rows - 1
        y = 0

        # y is not <= because cols should be len(matrix[0]) - 1
        # start from bottom left and moving up right
        while x >= 0 and y < cols:
            curr = matrix[x][y]

            if curr == target:
                return True
            elif curr > target:
                x -= 1
            else:
                y += 1

        return False


test = Solution()
print test.searchMatrix([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
], 4)