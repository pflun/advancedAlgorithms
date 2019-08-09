class Solution(object):
    def longestIncreasingPath(self, matrix):
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