# -*- coding: utf-8 -*-
# https://discuss.leetcode.com/topic/27098/python-solution-easy-to-understand
# 两部pass，先用 2／3 表示下一步活／死，再变回01
class Solution(object):
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