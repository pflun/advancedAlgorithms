# https://www.cnblogs.com/lightwindy/p/9739158.html
class Robot(object):
    def __init__(self):
        self.visited = set()
        self.dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        return

    def move(self):
        return True

    def turnLeft(self):
        return

    def turnRight(self):
        return

    def clean(self):
        return True

    def turnBack(self):
        robot.turnRight()
        robot.turnRight()

    def cleanRoom(self, robot):
        dfs(robot, 0, 0)

    # I think we need the exit
    def dfs(self, robot, x, y):
        robot.clean()
        self.visited.add(str(x) + '-' + str(y))
        for d in self.dir:
            newx = x + d[0]
            newy = y + d[1]
            if robot.move() and not self.visited(str(newx) + '-' + str(newy)):
                helper(robot, newx, newy)
                # backtracking to last position + direction, turnBack => move => turnBack
                robot.turnBack()
                robot.move()
                robot.turnBack()
            else:
                robot.turnRight()