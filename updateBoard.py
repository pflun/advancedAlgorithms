class Solution(object):
    def updateBoard(self, board, click):
        clickx = click[0]
        clicky = click[1]
        if board[clickx][clicky] == 'M':
            board[clickx][clicky] = 'X'
            return board

        queue = [click]

        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                if curr[0] < 0 or curr[0] == len(board) or curr[1] < 0 or curr[1] == len(board[0]) or board[curr[0]][curr[1]] != 'E':
                    continue
                adjmines = self.numsM(board, curr[0], curr[1])
                if adjmines != 0:
                    board[curr[0]][curr[1]] = str(adjmines)
                else:
                    board[curr[0]][curr[1]] = 'B'
                    dir = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [1, 1], [-1, 1], [1, -1]]
                    for d in dir:
                        currx = curr[0] + d[0]
                        curry = curr[1] + d[1]
                        queue.append([currx, curry])

        return board

    def numsM(self, board, x, y):
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [1, 1], [-1, 1], [1, -1]]
        counter = 0
        for d in dir:
            currx = x + d[0]
            curry = y + d[1]
            if currx < 0 or currx == len(board) or curry < 0 or curry == len(board[0]):
                continue
            if board[currx][curry] == 'M':
                counter += 1

        return counter

test = Solution()
print test.updateBoard(
    [['E', 'E', 'E', 'E', 'E'],
    ['E', 'E', 'M', 'E', 'E'],
    ['E', 'E', 'E', 'E', 'E'],
    ['E', 'E', 'E', 'E', 'E']], [3,0])