class Solution(object):
    def countBattleships(self, board):
        cnt = 0
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == 'X':
                    self.dfs(board, y, x)
                    cnt += 1
        return cnt

    def dfs(self, board, y, x):
        if x < 0 or y < 0 or x == len(board[0]) or y == len(board) or board[y][x] != 'X':
            return
        board[y][x] = 'x'
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for d in dir:
            curry = y + d[0]
            currx = x + d[1]
            self.dfs(board, curry, currx)

test = Solution()
print test.countBattleships([
    ['.', '.', '.', 'X'],
    ['X', 'X', '.', 'X'],
    ['.', '.', '.', 'X']
])