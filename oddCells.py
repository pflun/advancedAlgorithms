class Solution(object):
    def oddCells(self, n, m, indices):
        res = [['even' for _ in range(m)] for _ in range(n)]
        for indice in indices:
            for i in range(m):
                if res[indice[0]][i] == 'even':
                    res[indice[0]][i] = 'odd'
                elif res[indice[0]][i] == 'odd':
                    res[indice[0]][i] = 'even'
            for j in range(n):
                if res[j][indice[1]] == 'even':
                    res[j][indice[1]] = 'odd'
                elif res[j][indice[1]] == 'odd':
                    res[j][indice[1]] = 'even'
        cnt = 0
        for i in range(n):
            for j in range(m):
                if res[i][j] == 'odd':
                    cnt += 1
        return cnt, res

test = Solution()
print test.oddCells(2, 3, [[0,1],[1,1]])