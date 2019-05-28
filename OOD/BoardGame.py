class Board(object):
    def __init__(self):
        self.blackCount = 0
        self.whiteCount = 0
        # matrix, [row][col]
        self.board = []

    def init(self):
        pass

    def placeColor(self, row, col, color):
        pass

    def flip(self):
        pass

    def getScoreForColor(self, color):
        pass

class Piece(object):
    def __init__(self):
        self.color = ''

class Player(object):
    def __init__(self):
        self.color = ''

    def playPiece(self, row, col, color):
        return Board().placeColor(row, col, color)