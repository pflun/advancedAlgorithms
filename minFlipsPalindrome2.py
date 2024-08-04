# https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-ii/solutions/5581114/counting-greedy-python3/
# 4 way symmetry, change to all 1s or all 0s, whichever costs less
# 2 way symmetry, middle column & middle row,
#   count the number of (1, 1), and (1, 0) pair
#     if there's an even number of (1, 1) pair,
#       we can simply change all (1, 0) pair to (0, 0) to achive symmetry.
#     if there's an odd number of (1, 1) pair,
#       if we have at least one (1, 0) pair, change that (1, 0) pair to (1, 1)
#       if there's no (1, 0) pair, change one (1, 1) to (0, 0)
#   ignore (0, 0) pair, because we never change (0, 0) to (1, 1)
# center cell, if it's 1, always change to 0
class Solution(object):
    def minFlips(self, grid):
        res = single = double = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m / 2):
            for j in range(n / 2):
                # for each (i, j), there're other 3 cells should be the same
                # e.g. if ones is 3, we know 3 flips to make all to 0 and 1 flip to make all to 1
                ones = grid[i][j] + grid[m - 1 - i][j] + grid[m - 1 - i][n - 1 - j] + grid[i][n - 1 - j]
                res += min(ones, 4 - ones)
            if n % 2 == 1:
                ones = grid[i][n // 2] + grid[m - 1 - i][n // 2]
                single += (ones == 1)
                double += (ones == 2)
        if m % 2 == 1:
            for j in range(n / 2):
                ones = grid[m / 2][j] + grid[m // 2][n - 1 - j]
                single += (ones == 1)
                double += (ones == 2)
            if n % 2 == 1:
                res += grid[m / 2][n / 2]

        if double % 2 == 0 or single > 0:
            return res + single
        return res + 2

test = Solution()
print test.minFlips([[1,0,0],[0,1,0],[0,0,1]])
print test.minFlips([[0,1],[0,1],[0,0]])
print test.minFlips([[1],[1]])