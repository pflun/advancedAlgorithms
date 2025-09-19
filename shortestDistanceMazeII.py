# 505. Maze II
class Solution:
    def shortestDistance(self, maze, start, destination):
        queue = [start]
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        dist = [[float('inf')] * len(maze[0]) for _ in range(len(maze))]
        dist[start[0]][start[1]] = 0
        while queue:
            currx, curry = queue.pop(0)
            for d in dir:
                newx, newy = currx, curry  # deep copy
                k = dist[newx][newy]
                # move until hit a wall
                while 0 <= newx + d[0] < len(maze) and 0 <= newy + d[1] < len(maze[0]) and maze[newx + d[0]][newy + d[1]] == 0:
                    newx += d[0]
                    newy += d[1]
                    k += 1
                if k < dist[newx][newy]:
                    dist[newx][newy] = k
                    queue.append([newx, newy])

        return -1 if dist[destination[0]][destination[1]] == float('inf') else dist[destination[0]][destination[1]]

test = Solution()
print test.shortestDistance([
    [0,0,1,0,0],
    [0,0,0,0,0],
    [0,0,0,1,0],
    [1,1,0,1,1],
    [0,0,0,0,0]], [0,4], [4,4])
print test.shortestDistance([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4], [3,2])
print test.shortestDistance([[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], [4,3], [0,1])