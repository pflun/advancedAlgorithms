# -*- coding: utf-8 -*-
# https://discuss.leetcode.com/topic/27098/python-solution-easy-to-understand
# 两部pass，先用 2／3 表示下一步活／死，再变回01
from collections import Counter
class Solution(object):
    # in-place
    def gameOfLife2(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                lives = self.getLives(board, i, j)
                # 1
                if board[i][j] == 1 and lives < 2:
                    board[i][j] = 3
                # 2
                if board[i][j] == 1 and (lives == 2 or lives == 3):
                    continue
                # 3
                if board[i][j] == 1 and lives > 3:
                    board[i][j] = 3
                # 4
                if board[i][j] == 0 and lives == 3:
                    board[i][j] = 2

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0
        return board

    # 2/3 next live/die
    def getLives(self, board, i, j):
        cnt = 0
        for m in range(max(0, i - 1), min(len(board), i + 2)):
            for n in range(max(0, j - 1), min(len(board[0]), j + 2)):
                if m == i and n == j:
                    continue
                # 1不解释，3是 生 => 死，3也就是上一轮是生，所以上一轮升的是1，3
                if board[m][n] == 1 or board[m][n] == 3:
                    cnt += 1
        return cnt

    # infinite board, 每次读3行处理中间1行，第0行和最后一行读2行分开处理（python取出来直接改，不需要再赋值回去）
    def gameOfLifeInfiniteBoard(self, board):
        # row 0
        first = board[:2]
        for j in range(len(first)):
            lives = self.getLives(first, 0, j)
            if first[0][j] == 1 and lives < 2:
                first[0][j] = 3
            if first[0][j] == 1 and (lives == 2 or lives == 3):
                continue
            if first[0][j] == 1 and lives > 3:
                first[0][j] = 3
            if first[0][j] == 0 and lives == 3:
                first[0][j] = 2
        # row 1 to row n - 1
        n = len(board)
        for i in range(1, n - 1):
            middle = board[i - 1: i + 2]
            for j in range(len(middle)):
                lives = self.getLives(middle, 1, j)
                if middle[1][j] == 1 and lives < 2:
                    middle[1][j] = 3
                if middle[1][j] == 1 and (lives == 2 or lives == 3):
                    continue
                if middle[1][j] == 1 and lives > 3:
                    middle[1][j] = 3
                if middle[1][j] == 0 and lives == 3:
                    middle[1][j] = 2
        # last row
        last = board[-2:]
        for j in range(len(last)):
            lives = self.getLives(last, 1, j)
            if last[1][j] == 1 and lives < 2:
                last[1][j] = 3
            if last[1][j] == 1 and (lives == 2 or lives == 3):
                continue
            if last[1][j] == 1 and lives > 3:
                last[1][j] = 3
            if last[1][j] == 0 and lives == 3:
                last[1][j] = 2
        # board[n - 2:] = last
        for i in range(n):
            curr = board[i]
            for j in range(len(curr)):
                if curr[j] == 2:
                    curr[j] = 1
                elif curr[j] == 3:
                    curr[j] = 0
        return board

    # infinite board, sparse matrix
    def gameOfLifeInfiniteSparse(self, live):
        ctr = Counter((I, J)
                      for i, j in live
                      for I in range(i - 1, i + 2)
                      for J in range(j - 1, j + 2)
                      if I != i or J != j)
        print ctr
        return {ij
                for ij in ctr
                if ctr[ij] == 3 or ctr[ij] == 2 and ij in live}

    def gameOfLife(self, board):
        """
        :type board: List[List[int]], int = 0 dead,1 live
        " 2 dead -> live ; 3 live -> dead
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        if m == 0 or n == 0:
            return
        for iM in range(m):
            for iN in range(n):
                numNeighbor = sum([board[i][j]%2 for i in range(iM-1,iM+2) for j in range(iN-1,iN+2) if 0 <= i < m and 0<= j < n]) - board[iM][iN]
                if board[iM][iN] == 0 and numNeighbor == 3:
                    board[iM][iN] = 2
                if board[iM][iN] == 1 and ( numNeighbor < 2 or numNeighbor >  3):
                    board[iM][iN] = 3
        for iM in range(m):
            for iN in range(n):
                if board[iM][iN] == 2:
                    board[iM][iN] = 1
                if board[iM][iN] == 3:
                    board[iM][iN] = 0

test = Solution()
# print test.gameOfLife2([
#     [0,1,0],
#     [0,0,1],
#     [1,1,1],
#     [0,0,0]])
print test.gameOfLifeInfiniteBoard([
    [0,1,0],
    [0,0,1],
    [0,0,0],
    [0,0,1],
    [0,1,1],
    [0,0,1],
    [1,1,1],
    [0,0,0]])
# board = [
#     [0,1,0],
#     [0,0,1],
#     [1,1,1],
#     [0,0,0]]
# live = {(i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live}
# print test.gameOfLifeInfiniteSparse(live)