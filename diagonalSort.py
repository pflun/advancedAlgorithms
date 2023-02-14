class Solution(object):
    def diagonalSort(self, mat):
        dic = {}
        for y in range(len(mat)):
            for x in range(len(mat[0])):
                dic[y - x] = dic.get(y - x, []) + [mat[y][x]]
        for k, v in dic.items():
            dic[k] = sorted(v)
        for y in range(len(mat)):
            for x in range(len(mat[0])):
                curr = dic[y - x].pop(0)
                mat[y][x] = curr
        return mat

test = Solution()
print test.diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]])