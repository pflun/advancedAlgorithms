# https://www.youtube.com/watch?v=vkFUB--OYy0

class Solution(object):
    def maximalSquare(self, matrix):
        if len(matrix) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        sum = []
        res = 0

        # generate all zeros matrix
        for i in range(m + 1):
            tmp = []
            for j in range(n + 1):
                tmp.append(0)
            sum.append(tmp)

        # preprocess
        # sum: a rectangle from [0, 0] to [i, j]'s sum val (in this case, how many 1s in this area)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                sum[i][j] = int(matrix[i - 1][j - 1]) + sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # k range from 0 to min((m+1)-i, (n+1)-j) at bottom right
                # from largest -> smallest because if larger one meet k * k, no need to calculate smaller one
                for k in range(min(m - i + 1, n - j + 1), 0, -1):
                    # large square - two rectangle + small square
                    tmp = sum[i + k - 1][j + k - 1] - sum[i + k - 1][j - 1] - sum[i - 1][j + k - 1] + sum[i - 1][j - 1]

                    # if full
                    if tmp == k * k:
                        res = max(res, tmp)
                        break

        return res

test = Solution()
print test.maximalSquare([
    ["0", "0", "0"],
    ["1", "1", "0"],
    ["1", "1", "1"],
    ["1", "1", "1"]])


