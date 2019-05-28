class Solution(object):
    def imageSmoother(self, M):
        if not M:
            return []

        # empty matrix
        res = []
        for i in range(len(M)):
            tmp = []
            for j in range(len(M[0])):
                tmp.append(0)
            res.append(tmp)

        def average(M, sum, cell, i, j):
            dir = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [-1, 1], [1, -1]]
            sum += M[i][j]
            cell += 1
            for d in dir:
                curry = i + d[0]
                currx = j + d[1]
                if curry < 0 or curry == len(M) or currx < 0 or currx == len(M[0]):
                    continue
                sum += M[curry][currx]
                cell += 1

            return sum, cell

        for i in range(len(M)):
            for j in range(len(M[0])):
                sum, cell = average(M, 0, 0, i, j)
                res[i][j] = sum / cell

        return res

test = Solution()
print test.imageSmoother(
    [[1,1,1],
    [1,0,1],
    [1,1,1]])