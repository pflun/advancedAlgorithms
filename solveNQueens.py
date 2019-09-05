# https://www.youtube.com/watch?v=Xa-yETqFNEQ
class Solution(object):
    def solveNQueens(self, n):
        self.res = []

        def generateRow(y, x, n):
            res = ''
            for _ in range(x):
                res += '.'
            res += 'Q'
            for _ in range(x + 1, n):
                res += '.'
            return res

        def dfs(cols, rows, diag1, diag2, tmp, remain):
            if remain == 0:
                self.res.append(tmp[:])
                return

            y = 0
            while y < n:
                if y not in cols:
                    break
                y += 1
            for x in range(n):
                if x not in rows:
                    if x + y not in diag1 and y - x not in diag2:
                        cols.add(y)
                        rows.add(x)
                        diag1.add(x + y)
                        diag2.add(y - x)
                        tmp.append(generateRow(y, x, n))
                        dfs(cols, rows, diag1, diag2, tmp, remain - 1)
                        cols.remove(y)
                        rows.remove(x)
                        diag1.remove(x + y)
                        diag2.remove(y - x)
                        tmp.pop()

        dfs(set(), set(), set(), set(), [], n)
        return self.res

test = Solution()
print test.solveNQueens(4)