# 499. The Maze III
class Solution(object):
    def findShortestWay(self, maze, ball, hole):
        m, n = len(maze), len(maze[0])
        r, c = ball
        rh, ch = hole
        q = [(r, c)]
        # dist: how many steps to reach to [i][j]
        dist = [[float('inf')] * n for _ in range(m)]
        dist[r][c] = 0
        # path store shortest path's directions "dldr" at [i][j]
        path = [[None] * n for _ in range(m)]
        path[r][c] = ''
        while q:
            i, j = q.pop(0)
            # from stop to change direction
            for a, b, d in [(-1, 0, 'u'), (1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r')]:
                x, y, step = i, j, dist[i][j]
                # ball won't stop rolling until hitting a wall
                while (
                    0 <= x + a < m
                    and 0 <= y + b < n
                    and maze[x + a][y + b] == 0
                    and (x != rh or y != ch)
                ):
                    x, y = x + a, y + b
                    step += 1
                if dist[x][y] > step or (
                    dist[x][y] == step and path[i][j] + d < path[x][y]
                ):
                    # when find shorter or better lexicographical path, update dist && path
                    dist[x][y] = step
                    path[x][y] = path[i][j] + d
                    if x != rh or y != ch:
                        q.append((x, y))

        return path[rh][ch] or 'impossible'

test = Solution()
print test.findShortestWay([[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], [4,3], [0,1])
print test.findShortestWay([[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], [4,3], [3,0])
print test.findShortestWay([[0,0,0,0,0,0,0],[0,0,1,0,0,1,0],[0,0,0,0,1,0,0],[0,0,0,0,0,0,1]], [0,4], [3,5])