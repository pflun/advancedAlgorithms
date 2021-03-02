# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=yKr4iyQnBpY&ab_channel=HuaHua
# top down dp: dfs + cache
# dfs return the max path length starting at (x, y)
# 1 + dfs 所有neighbor最长路径最大值
# 这道题不会死循环，因为递归第一次出口在最大值位置，这个位置是base case自动为1，因为别的地方都更小所以这里的最长路径就为1
class Solution(object):
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0

        longest_path = 0
        rows = len(matrix)
        cols = len(matrix[0])
        cache = [[None] * cols for _ in range(rows)]

        def dfs(x, y):
            if cache[x][y]:
                return cache[x][y]
            longest_path = 0
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newX, newY = x + i, y + j
                if newX >= 0 and newX < rows and newY >= 0 and newY < cols and matrix[newX][newY] > matrix[x][y]:
                    longest_path = max(longest_path, dfs(newX, newY))
            cache[x][y] = longest_path + 1
            return cache[x][y]

        for x in range(rows):
            for y in range(cols):
                longest_path = max(longest_path, dfs(x, y))

        return longest_path

    def longestIncreasingPath2(self, matrix):
        self.res = 0
        self.dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(matrix, i, j, steps, prev):
            if i < 0 or j < 0 or i == len(matrix) or j == len(matrix[0]) or matrix[i][j] <= prev:
                return
            self.res = max(self.res, steps)
            for d in self.dir:
                curry = i + d[0]
                currx = j + d[1]
                dfs(matrix, curry, currx, steps + 1, matrix[i][j])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(matrix, i, j, 1, float('-inf'))

        return self.res

test = Solution()
print test.longestIncreasingPath([
  [3,4,5],
  [3,2,6],
  [2,2,1]
])