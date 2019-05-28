# -*- coding: utf-8 -*-
class Solution(object):
    def diceSum(self, ):
        self.res = []
        self.largerThanFifteen = 0
        # 3 dices
        self.A = [1, 2, 3, 4, 5, 6]
        self.B = [1, 2, 3, 4, 5, 6]
        self.C = [1, 2, 3, 4, 5, 6]

        # backtracking
        def dfs(tmp):
            if len(tmp) == 3:
                tmpSum = sum(tmp[:])
                if tmpSum > 15:
                    self.largerThanFifteen += 1
                self.res.append(tmpSum)
                return
            if len(tmp) == 0:
                for i in range(len(self.A)):
                    tmp.append(self.A[i])
                    dfs(tmp)
                    tmp.pop()
            elif len(tmp) == 1:
                for i in range(len(self.B)):
                    tmp.append(self.B[i])
                    dfs(tmp)
                    tmp.pop()
            elif len(tmp) == 2:
                for i in range(len(self.C)):
                    tmp.append(self.C[i])
                    dfs(tmp)
                    tmp.pop()
        dfs([])
        return self.largerThanFifteen, len(self.res)

    def nDiceSum(self, n):
        self.res = []
        self.largerThanFifteen = 0
        # dice
        self.dice = [1, 2, 3, 4, 5, 6]

        # backtracking
        def dfs(tmp):
            if len(tmp) == n:
                tmpSum = sum(tmp[:])
                if tmpSum > 15:
                    self.largerThanFifteen += 1
                self.res.append(tmpSum)
                return
            elif len(tmp) < n:
                for i in range(len(self.dice)):
                    tmp.append(self.dice[i])
                    dfs(tmp)
                    tmp.pop()

        dfs([])
        return self.largerThanFifteen, len(self.res)

test = Solution()
print test.nDiceSum(4)