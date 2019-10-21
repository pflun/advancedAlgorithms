class TicTacToe(object):
    def __init__(self):
        self.matrix = [['-' for _ in range(3)] for _ in range(3)]
        self.rows = [0 for _ in range(3)]
        self.cols = [0 for _ in range(3)]
        self.diag = 0
        self.revDiag = 0

    def printBoard(self):
        res = [[None for _ in range(5)] for _ in range(3)]
        for i in range(3):
            res[i][1] = '|'
            res[i][3] = '|'
        for i in range(3):
            res[i][0] = self.matrix[i][0]
            res[i][2] = self.matrix[i][1]
            res[i][4] = self.matrix[i][2]
        for i in range(3):
            print ''.join(res[i])

    def move(self, row, col, player):
        self.matrix[row][col] = player
        # player: X, AI: O
        if player == 'X':
            add = 1
        else:
            add = -1
        self.rows[row] += add
        self.cols[col] += add
        if row == col:
            self.diag += add
        if row + col == 2:
            self.revDiag += add
        if abs(self.rows[row]) == 3 or abs(self.cols[col]) == 3 or abs(self.diag) == 3 or abs(self.revDiag) == 3:
            return player  # player: X, AI: O
        else:
            return 0

test = TicTacToe()
test.printBoard()
test.move(1, 1, 'X')
test.printBoard()