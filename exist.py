# LC 212 Word Search
class Solution(object):
    def exist(self, board, word):
        if not board or not word:
            return 0

        depth = len(word)

        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, depth, word, res)

        return any(res)

    def dfs(self, board, i, j, depth, word, res):

        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[0]:
            return
        if len(word) == 1:
            res.append(True)
            return
        if depth == 0:
            return

        # Trick to replace Visited, set board[i][j] to '#' to avoid visit again, NEED add back after dfs (backtrace)
        tmp = board[i][j]
        board[i][j] = "#"
        self.dfs(board, i + 1, j, depth - 1, word[1:], res)
        self.dfs(board, i - 1, j, depth - 1, word[1:], res)
        self.dfs(board, i, j + 1, depth - 1, word[1:], res)
        self.dfs(board, i, j - 1, depth - 1, word[1:], res)
        board[i][j] = tmp



test = Solution()
print test.exist(
 [['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']], "ABCCED")
