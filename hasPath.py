# 490. The Maze I
class Solution(object):
    def hasPath(self, maze, start, destination):
        queue = [start]
        visited = set() # same as set([(start[0], start[1])])
        visited.add((start[0], start[1]))
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue:
            currx, curry = queue.pop(0)
            for d in dir:
                newx, newy = currx, curry # deep copy
                # move until hit a wall
                while 0 <= newx + d[0] < len(maze) and 0 <= newy + d[1] < len(maze[0]) and maze[newx + d[0]][newy + d[1]] == 0:
                    newx = newx + d[0]
                    newy = newy + d[1]
                if [newx, newy] == destination:
                    return True
                if (newx, newy) not in visited:
                    visited.add((newx, newy))
                    queue.append([newx, newy])
        return False

test = Solution()
print test.hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4], [4,4])
print test.hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4], [3,2])
print test.hasPath([[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], [4,3], [0,1])
