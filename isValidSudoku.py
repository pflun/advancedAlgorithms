class Solution(object):
    def isValidSudoku(self, board):
        # row
        for j in range(len(board)):
            used = set()
            for i in range(len(board[0])):
                if board[j][i] in used:
                    return False
                elif board[j][i] == '.':
                    continue
                else:
                    used.add(board[j][i])

        # column
        for i in range(len(board[0])):
            used = set()
            for j in range(len(board)):
                if board[j][i] in used:
                    return False
                elif board[j][i] == '.':
                    continue
                else:
                    used.add(board[j][i])

        # 3 * 3 square
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                if not self.isValid(board, x, y):
                    return False

        return True

    def isValid(self, board, x, y):
        used = set()
        for j in range(y, y + 3):
            for i in range(x, x + 3):
                if board[j][i] in used:
                    return False
                elif board[j][i] == '.':
                    continue
                else:
                    used.add(board[j][i])
        return True

test = Solution()
print test.isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
])