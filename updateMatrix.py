# Need Debug

class Solution(object):
    def updateMatrix(self, matrix):
        if len(matrix) == 0:
            return

        m, n, queue = len(matrix), len(matrix[0]), []
        res = []

        def bfs(i, j, depth, visited):
            if i < 0 or i > m-1 or j < 0 or j > n-1:
                return
            if [i, j] in visited:
                return
            else:
                visited.append([i, j])

            queue.append((i, j))
            # print i, j, depth, visited, queue

            if matrix[i][j] == 0:
                if self.distance == 0 and depth != 0:
                    self.distance = depth
                elif self.distance != 0 and depth != 0:
                    self.distance = min(self.distance, depth)
                print i, j, depth, visited, queue
                return

            while queue:
                # print queue
                curr = queue.pop(0)
                i, j = curr[0], curr[1]
                # print i, j
                bfs(i+1, j, depth + 1, visited)
                bfs(i-1, j, depth + 1, visited)
                bfs(i, j+1, depth + 1, visited)
                bfs(i, j-1, depth + 1, visited)

        for i in range(len(matrix)):
            tmp = []
            for j in range(len(matrix)):
                depth = 0
                self.distance = 0
                visited = []
                queue = []
                print 'hi', i, j
                bfs(i, j, depth, visited)
                tmp.append(self.distance)
            res.append(tmp)

        return res

class Solution2(object):
    def updateMatrix(self, matrix):
        if len(matrix) == 0:
            return

        m, n, queue = len(matrix), len(matrix[0]), []

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == 0:
                    queue.append([i, j])
                else:
                    matrix[i][j] = float("inf")

        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue:
            curr = queue.pop(0)
            i, j = curr[0], curr[1]
            for d in dir:
                row = i + d[0]
                col = j + d[1]
                if row < 0 or row > m - 1 or col < 0 or col > n - 1 or matrix[row][col] <= matrix[i][j] + 1:
                    continue
                queue.append([row, col])
                matrix[row][col] = matrix[i][j] + 1

        return matrix

class Solution3(object):
    def updateMatrix(self, matrix):
        if len(matrix) == 0:
            return matrix

        res = []
        for _ in range(len(matrix)):
            tmp = []
            for _ in range(len(matrix[0])):
                tmp.append(0)
            res.append(tmp)

        for i in range(len(res)):
            for j in range(len(res[0])):
                if matrix[i][j] != 0:
                    cell = self.bfs(matrix, i, j)
                    res[i][j] = cell

        return res

    def bfs(self, matrix, x, y):
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set((x, y))
        queue = [[x, y]]
        counter = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.pop()
                for d in dir:
                    currx = curr[0] + d[0]
                    curry = curr[1] + d[1]
                    if currx < 0 or currx == len(matrix) or curry < 0 or curry == len(matrix[0]) or (currx, curry) in visited:
                        continue
                    if matrix[currx][curry] == 0:
                        return counter
                    visited.add((currx, curry))
                    queue.append([currx, curry])

            counter += 1

        return -1

test = Solution3()
print test.updateMatrix([
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1]])
