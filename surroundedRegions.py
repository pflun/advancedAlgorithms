# -*- coding: utf-8 -*-
# Any O that not connect to border will become X, so start from 4 borders

class Solution:
    # @param {list[list[str]]} board a 2D board containing 'X' and 'O'
    # @return nothing
    def surroundedRegions(self, board):
        def fill(x, y):
            if x < 0 or x > m-1 or y < 0 or y > n-1 or board[x][y] != 'O':
                return
            queue.append((x, y))
            board[x][y] = 'D'

        def bfs(x, y):
            if board[x][y] == 'O':
                queue.append((x, y))
                fill(x, y)

            while queue:
                curr = queue.pop(0)
                i, j = curr[0], curr[1]
                fill(i+1, j)
                fill(i-1, j)
                fill(i, j+1)
                fill(i, j-1)

        if len(board) == 0:
            return
        m, n, queue = len(board), len(board[0]), []
        for i in range(n):
            # start from 4 borders
            bfs(0, i)
            bfs(m-1, i)

        for j in range(1, m-1):
            # start from 4 borders
            bfs(j, 0)
            bfs(j, n-1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'D':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

        return board

    # DFS, 所有不与边上的O相连的O都会变成X。
    def surroundedRegionsDFS(self, board):

        def dfs(x, y):
            if x < 0 or x > m-1 or y < 0 or y > n-1 or board[x][y] != 'O':
                return
            # DFS所有与边相连的 O 都变成 D，与边不相连DFS不到的还是 O
            board[x][y] = 'D'
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        m, n = len(board), len(board[0])
        # 扫四条边，看边上有没有O
        for i in range(n):
            # 边上找到O点，从这点开始往里DFS
            if board[0][i] == 'O':
                board[0][i] = 'D'
                dfs(0, i)

            if board[m - 1][i] == 'O':
                board[m - 1][i] = 'D'
                dfs(m - 1, i)

        for j in range(1, m - 1):
            if board[j][0] == 'O':
                board[j][0] = 'D'
                dfs(j, 0)

            if board[j][n - 1] == 'O':
                board[j][n - 1] = 'D'
                dfs(j, n - 1)

        # 所有找到的 D 都是与边相连的，变成 O，剩下DFS不到的那些 O 都会变成 X
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'D':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

        return board

test = Solution()
print test.surroundedRegionsDFS([['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']])