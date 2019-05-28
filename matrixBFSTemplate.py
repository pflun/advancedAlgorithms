# Please see Amazon-golfMaze.py

class Solution(object):
    def matrixBFSTemplate(self, matrix):
        if len(matrix) == 0:
            return

        m, n, queue = len(matrix), len(matrix[0]), []
        res = []

        def bfs(i, j, visited):
            visited.append([i, j])
            queue.append((i, j))

            dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while queue:
                curr = queue.pop(0)
                i, j = curr[0], curr[1]

                for d in dir:
                    row = i + d[0]
                    col = j + d[1]
                    if row < 0 or row > m - 1 or col < 0 or col > n - 1 or [row, col] in visited:
                        continue
                    print matrix[row][col]
                    visited.append([row, col])
                    queue.append([row, col])

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                visited = []
                queue = []
                print 'hi', i, j
                bfs(i, j, visited)

        print "============================================================================="


test = Solution()
print test.matrixBFSTemplate([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]])
