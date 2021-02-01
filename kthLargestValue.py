class Solution(object):
    def kthLargestValue(self, matrix, k):
        xor = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 and j == 0:
                    xor[i][j] = matrix[i][j]
                    res.append(xor[i][j])
                    continue
                if i == 0:
                    xor[i][j] = matrix[i][j] ^ xor[i][j - 1]
                    res.append(xor[i][j])
                    continue
                if j == 0:
                    xor[i][j] = matrix[i][j] ^ xor[i - 1][j]
                    res.append(xor[i][j])
                    continue
                xor[i][j] = matrix[i][j] ^ xor[i - 1][j] ^ xor[i][j - 1] ^ xor[i - 1][j - 1]
                res.append(xor[i][j])
        res.sort(reverse=True)
        return res[k - 1]

test = Solution()
print test.kthLargestValue([[5,2],[1,6]], 1)
print test.kthLargestValue([[5,2],[1,6]], 2)
print test.kthLargestValue([[5,2],[1,6]], 4)