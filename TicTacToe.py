# -*- coding: utf-8 -*-
# https://www.cnblogs.com/grandyang/p/5467118.html
# 建立一个大小为n的一维数组rows和cols，还有变量对角线diag和逆对角线rev_diag，如果玩家1在第一行某一列放了一个子
# 那么rows[0]自增1，如果玩家2在第一行某一列放了一个子，则rows[0]自减1，那么只有当rows[0]等于n或者-n的时候
# 表示第一行的子都是一个玩家放的，则游戏结束返回该玩家即可
class TicTacToe(object):
    def __init__(self, n):
        self.rows = [0 for _ in range(n)]
        self.cols = [0 for _ in range(n)]
        self.diag = 0
        self.revDiag = 0
        # 最终胜利需要某一行一列达到N
        self.N = n

    def move(self, row, col, player):
        if player == 1:
            add = 1
        else:
            add = -1
        self.rows[row] += add
        self.cols[col] += add
        # 只有对角线和反对角线才会对胜利产生影响
        if row == col:
            self.diag += add
        if row + col == self.N - 1:
            self.revDiag += add
        if abs(rows[row]) == self.N or abs(cols[col]) == self.N or abs(self.diag) == self.N or abs(self.revDiag) == self.N:
            return player
        else:
            return 0