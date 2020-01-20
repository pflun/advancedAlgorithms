class Solution(object):
    def maxSideLength(self, mat, threshold):
        res = 0
        sum = [[0 for _ in range(len(mat[0]) + 1)] for _ in range(len(mat) + 1)]
        for i in range(1, len(mat) + 1):
            for j in range(1, len(mat[0]) + 1):
                sum[i][j] = int(mat[i - 1][j - 1]) + sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1]

        for i in range(1, len(mat) + 1):
            for j in range(1, len(mat[0]) + 1):
                for k in range(1, min(len(mat) - i + 1, len(mat[0]) - j + 1)):
                    # large square - two rectangle + small square
                    tmp = sum[i + k - 1][j + k - 1] - sum[i + k - 1][j - 1] - sum[i - 1][j + k - 1] + sum[i - 1][j - 1]
                    print k, tmp
                    if tmp > threshold:
                        break
                    else:
                        res = max(res, k)

        return res

test = Solution()
print test.maxSideLength([[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], 4)
print test.maxSideLength([[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], 1)
print test.maxSideLength([[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], 6)
print test.maxSideLength([[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], 40184)