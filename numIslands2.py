class Solution(object):
    def numIslands2(self, m, n, positions):
        res = []
        island = 0
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        for pos in positions:
            cnt = self.getOnes(matrix, pos)
            island += 1 - cnt
            res.append(island)
            matrix[pos[0]][pos[1]] = 1

        return res

    def getOnes(self, matrix, pos):
        cnt = 0
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for d in dir:
            curry = pos[0] + d[0]
            currx = pos[1] + d[1]
            if curry < 0 or currx < 0 or curry == len(matrix) or currx == len(matrix[0]):
                continue
            if matrix[curry][currx] == 1:
                cnt += 1
        return cnt

test = Solution()
print test.numIslands2(3, 3, [[0,0], [0,1], [1,2], [2,1]])