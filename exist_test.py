# Same solution to exist.py, use extra space visited[] as record
class Solution(object):
    def exist(self, board, word):
        if not board or not word:
            return 0

        depth = len(word)

        res = []
        visited = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, depth, word, res, visited)

        return any(res)

    def dfs(self, board, i, j, depth, word, res, visited):
        print i, j, word, res, visited

        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[0]:
            return
        if [i, j] in visited:
            return
        else:
            visited.append([i, j])

        if len(word) == 1:
            res.append(True)
            return
        if depth == 0:
            return

        # Trick to replace Visited, set board[i][j] to '#' to avoid visit again, NEED add back after dfs
        self.dfs(board, i + 1, j, depth - 1, word[1:], res, visited)
        self.dfs(board, i - 1, j, depth - 1, word[1:], res, visited)
        self.dfs(board, i, j + 1, depth - 1, word[1:], res, visited)
        self.dfs(board, i, j - 1, depth - 1, word[1:], res, visited)
        visited.pop()
        print visited


test = Solution()
print test.exist(
 [['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']], "SEE")
