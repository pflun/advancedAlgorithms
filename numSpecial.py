class Solution(object):
    def numSpecial(self, mat):
        res = 0
        col = {}
        row = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    col[i] = col.get(i, 0) + 1
                    row[j] = row.get(j, 0) + 1

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    if col[i] == 1 and row[j] == 1:
                        res += 1

        return res

test = Solution()
print test.numSpecial([
    [0,0,0,1],
    [1,0,0,0],
    [0,1,1,0],
    [0,0,0,0]])
print test.numSpecial([
    [0,0,0,0,0],
    [1,0,0,0,0],
    [0,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,1]])