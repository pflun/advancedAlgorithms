# -*- coding: utf-8 -*-
# 给一个4*4的matirx 由 16个大写字母组成。再给一个dictionary
# matrix里面的每一个cell可以走8个方向。horizontal, vertical, diaganal。问所有由这个matrix产生的词是不是都在给的dictionary里面
# 一个cell只能用一次
class Solution(object):
    def wordSearch(self, matrix, dictionary):
        self.res = []

        def dfs(matrix, word, index, i, j, visited):
            if i < 0 or i == len(matrix) or j < 0 or j == len(matrix[0]) or (i, j) in visited:
                return
            visited.add((i, j))
            if index == len(word) - 1 and matrix[i][j] == word[index]:
                self.res.append(word)
            elif matrix[i][j] == word[index]:
                dir = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]
                for d in dir:
                    curry = i + d[0]
                    currx = j + d[1]
                    dfs(matrix, word, index + 1, curry, currx, visited)

        for word in dictionary:
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == word[0]:
                        visited = set()
                        dfs(matrix, word, 0, i, j, visited)

        return self.res

test = Solution()
print test.wordSearch(
 [['o','a','a','n'],
  ['e','t','e','n'],
  ['i','k','h','p'],
  ['i','f','l','v']], ["oath","pea","eat","rain"])
