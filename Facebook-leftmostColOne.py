# In a binary matrix (all elements are 0 and 1), every row is sorted in ascending order (0 to the left of 1).
# Find the leftmost column index with a 1 in it.
# Template: binary search find first element larger than (in our case find 1 bc 1 > 0)
class Solution(object):
    def leftmostColOne(self, matrix):
        left = 0
        right = len(matrix[0]) - 1
        while left < right:
            mid = (left + right) / 2
            if not self.hasOne(matrix, mid):
                left = mid + 1
            else:
                right = mid
        return left

    def hasOne(self, matrix, col):
        for i in range(len(matrix)):
            if matrix[i][col] == 1:
                return True
        return False

test = Solution()
print test.leftmostColOne([
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 0]])
