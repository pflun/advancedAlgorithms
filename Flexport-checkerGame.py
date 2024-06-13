# -*- coding: utf-8 -*-
class Solution(object):
    # return possible move，最后返回一个List<List<Coordinate>>
    # OO
    # XX
    def nextMove(self, board, player):
        if player == 'O':
            offset = 1
        elif player == 'X':
            offset = -1
        res = [[[] for _ in range(len(board[0]))] for _ in range(len(board))]
        for j in range(len(board)):
            for i in range(len(board[0])):
                if board[j][i] == player:
                    nextPos = [[j + offset, i - offset], [j + offset, i + offset]]
                    # 不考虑吃
                    for p in nextPos:
                        if p[0] >= 0 and p[0] < len(board) and p[1] >= 0 and p[1] < len(board) and board[p[0]][p[1]] is None:
                            res[j][i].append(p)
        return res

test = Solution()
print test.nextMove([['O', None, 'O', None],
                     [None, None, None, None],
                     [None, None, None, None],
                     ['X', None, 'X', None]], 'O')
