class Solution(object):
    def luckyNumbers(self, matrix):
        candidates = []
        for i in range(len(matrix)):
            x = i
            y = 0
            for j in range(1, len(matrix[0])):
                if matrix[i][j] < matrix[x][y]:
                    x = i
                    y = j
            candidates.append([x, y])
        res = []
        for c in candidates:
            tmp = matrix[c[0]][c[1]]
            for i in range(len(matrix)):
                if i != c[0] and matrix[i][c[1]] > tmp:
                    tmp = False
            if tmp:
                res.append(tmp)
        return res

test = Solution()
print test.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]])
print test.luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]])
print test.luckyNumbers([[7,8],[1,2]])