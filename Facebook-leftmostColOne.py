# -*- coding: utf-8 -*-
# In a binary matrix (all elements are 0 and 1), every row is sorted in
# ascending order (0 to the left of 1). Find the leftmost column index with a 1 in it.
#
# Example 1:
#
# Input:
# [[0, 0, 0, 1],
#  [0, 0, 1, 1],
#  [0, 1, 1, 1],
#  [0, 0, 0, 0]]
# Output: 1
# Example 2:
#
# Input:
# [[0, 0, 0, 0],
#  [0, 0, 0, 0],
#  [0, 0, 0, 0],
#  [0, 0, 0, 0]]
# Output: -1
# Expected solution better than O(r * c).
# In a binary matrix (all elements are 0 and 1), every row is sorted in ascending order (0 to the left of 1).
# Find the leftmost column index with a 1 in it.
# Template: binary search find first element larger than (in our case find 1 bc 1 > 0)
class Solution(object):
    # O(m + n)
    def leftmostColOne2(self, matrix):
        # h pointer move right to left, v move top to bottom, start from top right
        h = len(matrix[0]) - 1
        v = 0

        # 维持matrix[v][h]一直在该行的1的最左端，一路向左下走
        while h >= 0 and v < len(matrix):
            if matrix[v][h] == 1:
                h -= 1
            else:
                v += 1
        if h < 0:
            return 0
        elif h == len(matrix[0]) - 1:
            return -1
        else:
            return h + 1  # h是最右全0的列

    # binary search
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
