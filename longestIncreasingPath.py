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

        res = 0
        rows = len(matrix)
        cols = len(matrix[0])
        cache = [[None] * cols for _ in range(rows)]

        def dfs(x, y):
            if cache[x][y]:
                return cache[x][y]
            tmp = 0
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newX, newY = x + i, y + j
                if newX >= 0 and newX < rows and newY >= 0 and newY < cols and matrix[newX][newY] > matrix[x][y]:
                    tmp = max(tmp, dfs(newX, newY))
            cache[x][y] = tmp + 1
            return cache[x][y]

        for x in range(rows):
            for y in range(cols):
                res = max(res, dfs(x, y))

        return res

    def longestIncreasingPath2(self, matrix):
        self.res = 0
        self.dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        memo = {}

        # 返回“从 (i, j) 往下走的最长步数”
        def dfs(i, j, prev):
            if i < 0 or j < 0 or i == len(matrix) or j == len(matrix[0]) or matrix[i][j] <= prev:
                return 0
            
            # 查缓存：如果这个格子之前算过了，直接交答案！
            if (i, j) in memo:
                return memo[(i, j)]
            
            max_neighbor_steps = 0
            for d in self.dir:
                curry = i + d[0]
                currx = j + d[1]
                # 递归去问周围四个邻居，它们能走多远？取最大值
                max_neighbor_steps = max(max_neighbor_steps, dfs(curry, currx, matrix[i][j]))
            
            # 存缓存：当前格子的最长路径 = 1 (格子自己) + 邻居能走的最远步数
            memo[(i, j)] = 1 + max_neighbor_steps
            return memo[(i, j)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.res = max(self.res, dfs(i, j, float('-inf')))

        return self.res

test = Solution()
print test.longestIncreasingPath([
  [3,4,5],
  [3,2,6],
  [2,2,1]
])