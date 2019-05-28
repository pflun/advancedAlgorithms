class Solution:

    # Simplest solution: convert matrix to big list, then binary search

    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """

    # Binary search Once
    def findPosition(self, matrix, target):
        if len(matrix) == 0:
            return False
        n, m = len(matrix), len(matrix[0])
        start, end = 0, n * m -1
        while start + 1 < end:
            mid = (start + end) / 2
            x, y = mid / m, mid % m
            if matrix[x][y] < target:
                start = mid
            else:
                end = mid
        x, y = start / m, start % m
        if matrix[x][y] == target:
            return True

        x, y = end / m, end % m
        if matrix[x][y] == target:
            return True

        return False

    def searchMatrix(self, matrix, target):

        if not matrix or target is None:
            return False

        rows = len(matrix)
        cols = len(matrix[0])
        low = 0
        high = rows * cols - 1

        while low <= high:
            mid = (low + high) / 2
            num = matrix[mid / cols][mid % cols]
            # print mid, num

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1

        return False



test = Solution()
print test.findPosition([
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 4)