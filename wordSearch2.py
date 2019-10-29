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

    def findWords2(self, board, words):
        self.res = []
        self.dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(board, tmp, target, visited, i, j):
            if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or (i, j) in visited or board[i][j] != target[0]:
                return
            target = target[1:]
            tmp += board[i][j]
            visited.add((i, j))
            if len(target) == 0:
                self.res.append(tmp)
                return
            for d in self.dir:
                x = i + d[0]
                y = j + d[1]
                dfs(board, tmp, target, visited, x, y)
            visited.remove((i, j))

        for word in words:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    dfs(board, '', word, set(), i, j)

        return self.res

test = Solution()
print test.findWords2(
 [['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']], ["oath","pea","eat","rain"])