# bug, shouldn't convert to int then add to set
class Solution(object):
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                elif board[i][j].isdigit():
                    rows[i].add(int(board[i][j]))
                    cols[j].add(int(board[i][j]))
                    bi = i / 3
                    bj = j / 3
                    boxes[bi][bj].add(int(board[i][j]))

        def dfs(board, rows, cols, boxes):
            # valid
            if all(len(r) == 9 for r in rows) and all(len(c) == 9 for c in cols) and all(len(b) == 9 for b in boxes):
                return True, board
            # backtracking
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == '.':
                        for n in range(1, 10):
                            # invalid
                            if n in rows[i] or n in cols[j] or n in boxes[i / 3][j / 3]:
                                continue
                            board[i][j] = n
                            rows[i].add(int(board[i][j]))
                            cols[j].add(int(board[i][j]))
                            bi = i / 3
                            bj = j / 3
                            boxes[bi][bj].add(int(board[i][j]))
                            found, candidate = dfs(board, rows, cols, boxes)
                            if found:
                                return found, candidate
                            board[i][j] = '.'
                            rows[i].remove(int(board[i][j]))
                            cols[j].remove(int(board[i][j]))
                            boxes[bi][bj].remove(int(board[i][j]))
            return False, []

        found, res = dfs(board, rows, cols, boxes)
        if found:
            return res
        else:
            return []
