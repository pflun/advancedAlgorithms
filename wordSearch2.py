# -*- coding: utf-8 -*-
class Solution(object):
    def findWords(self, board, words):
        self.res = []

        def dfs(board, i, j, depth, word):
            # 出界，depth为0，当前cell不等于word当前位
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or depth == 0 or board[i][j] != word[len(word) - depth]:
                return
            if depth == 1:
                self.res.append(word)

            # same letter cell may not be used more than once, backtracking
            tmp = board[i][j]
            board[i][j] = "#"
            dfs(board, i + 1, j, depth - 1, word)
            dfs(board, i - 1, j, depth - 1, word)
            dfs(board, i, j + 1, depth - 1, word)
            dfs(board, i, j - 1, depth - 1, word)
            board[i][j] = tmp


        for word in words:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    dfs(board, i, j, len(word), word)

        return self.res


test = Solution()
print test.findWords(
 [['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']], ["oath","pea","eat","rain"])