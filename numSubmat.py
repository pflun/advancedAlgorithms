class Solution(object):
    # TLE
    def numSubmat(self, mat):
        if len(mat) == 0:
            return 0
        m, n = len(mat), len(mat[0])
        sum = []
        res = 0

        # generate all zeros mat
        for i in range(m + 1):
            tmp = []
            for j in range(n + 1):
                tmp.append(0)
            sum.append(tmp)

        # preprocess
        # sum: a rectangle from [0, 0] to [i, j]'s sum val (in this case, how many 1s in this area)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                sum[i][j] = int(mat[i - 1][j - 1]) + sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for x in range(m - i + 1, 0, -1):
                    for y in range(n - j + 1, 0, -1):
                        tmp = sum[i + x - 1][j + y - 1] - sum[i + x - 1][j - 1] - sum[i - 1][j + y - 1] + sum[i - 1][j - 1]
                        if tmp == x * y:
                            res += 1
        return res

test = Solution()
print test.numSubmat2([[1,0,1],
              [1,1,0],
              [1,1,0]])
print test.numSubmat2([[0,1,1,0],
              [0,1,1,1],
              [1,1,1,0]])
print test.numSubmat2([[1,1,1,1,1,1]])
print test.numSubmat2([[1,0,1],[0,1,0],[1,0,1]])