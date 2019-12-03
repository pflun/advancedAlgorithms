class Solution(object):
    def __init__(self):
        self.rows = [0 for _ in range(3)]
        self.cols = [0 for _ in range(3)]
        self.diag = 0
        self.revDiag = 0

    def tictactoe(self, moves):
        for i in range(len(moves)):
            if i % 2 == 0:
                player = 'A'
                add = 1
            else:
                player = 'B'
                add = -1
            m = moves[i]
            self.rows[m[0]] += add
            self.cols[m[1]] += add
            if m[0] == m[1]:
                self.diag += add
            if m[0] + m[1] == 2:
                self.revDiag += add
            if abs(self.rows[m[0]]) == 3 or abs(self.cols[m[1]]) == 3 or abs(self.diag) == 3 or abs(self.revDiag) == 3:
                return player
        if len(moves) < 9:
            return "Pending"
        else:
            return "Draw"

test = Solution()
# print test.tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]])
# print test.tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]])
# print test.tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]])
print test.tictactoe([[0,0],[1,1]])