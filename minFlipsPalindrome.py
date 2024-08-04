class Solution(object):
    def minFlips(self, grid):
        # row palindrome
        res_row = 0
        for row in grid:
            res_row += self.numFlips(row)
        # col palindrome
        res_col = 0
        for j in range(len(grid[0])):
            tmp = [grid[i][j] for i in range(len(grid))]
            res_col += self.numFlips(tmp)

        return min(res_row, res_col)

    def numFlips(self, arr):
        res = 0
        i = 0
        j = len(arr) - 1
        while i < j:
            if arr[i] != arr[j]:
                res += 1
            i += 1
            j -= 1
        return res

test = Solution()
print test.minFlips([[1,0,0],[0,0,0],[0,0,1]])
print test.minFlips([[0,1],[0,1],[0,0]])
print test.minFlips([[1],[0]])