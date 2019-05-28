# Mine need debug, please see dfs solution at https://leetcode.com/articles/the-maze/
class Solution(object):
    def maze1(self, matrix, start, destination):
        if len(matrix) == 0:
            return

        visited = set()
        def dfs(matrix, i, j, visited, destination):
            if i < 0 or i == len(matrix) or j < 0 or j == len(matrix[0]) or matrix[i][j] == 1 or (i, j) in visited:
                return
            if i == destination[0] and j == destination[1]:
                return True
            visited.add((i, j))

            dir = findDirections(matrix, i, j)

            if len(dir) != 0:
                for d in dir:
                    next = nextPos(matrix, i, j, d)
                    print next, d
                    dfs(matrix, next[0], next[1], visited, destination)

        # return [[-1, 0], [0, 1]] means left and down are available
        def findDirections(matrix, i, j):
            res = []
            dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for d in dir:
                x = i + d[1]
                y = j + d[0]
                if x < 0 or x == len(matrix[0]) or y < 0 or y == len(matrix) or matrix[x][y] == 1:
                    continue
                res.append(d)

            return res

        # return next stop position for a direction, ie. [0, 4] go down will stop at [2, 4]
        def nextPos(matrix, i, j, dir):
            dirx = dir[0]
            diry = dir[1]

            if dirx == 0:
                while i + diry >= 0 and i + diry < len(matrix) and matrix[i + diry][j] == 0:
                    i += diry
            else:
                while j + dirx >= 0 and j + dirx < len(matrix[0]) and matrix[i][j + dirx] == 0:
                    j += dirx

            return [i, j]

        dfs(matrix, start[0], start[1], visited, destination)

        return False


test = Solution()
print test.maze1([
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]], [0, 4], [4, 4])
