class Solution(object):
    def countSquares(self, matrix):
        if len(matrix) == 0:
            return 0
        res = 0
        preSum = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        preSum[0][0] = matrix[0][0]
        if matrix[0][0] == 1:
            res += 1
        for j in range(1, len(matrix[0])):
            preSum[0][j] = matrix[0][j] + preSum[0][j - 1]
            if matrix[0][j] == 1:
                res += 1
        for i in range(1, len(matrix)):
            preSum[i][0] = matrix[i][0] + preSum[i - 1][0]
            if matrix[i][0] == 1:
                res += 1
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                preSum[i][j] = preSum[i][j - 1] + preSum[i - 1][j] + matrix[i][j] - preSum[i - 1][j - 1]
                if matrix[i][j] == 1:
                    res += 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                for k in range(2, min(len(matrix) - i, len(matrix[0]) - j)):
                    # print k, i, j
                    tmp = preSum[i + k][j + k] - preSum[i][j + k] - preSum[i + k][j] + preSum[i][j]
                    print tmp, k, i, j
                    if tmp == k * k:
                        # print k, i, j
                        res += 1
        return res

    def countSquares2(self, matrix):
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
                        res += 1

        return res

test = Solution()
print test.countSquares2([
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
])
print test.countSquares2([
  [1,0,1],
  [1,1,0],
  [1,1,0]
])