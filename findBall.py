class Solution(object):
    def findBall(self, grid):
        stuck = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if j + 1 < len(grid[0]) and grid[i][j] == 1 and grid[i][j + 1] == -1:
                    stuck.add(str(i) + "_" + str(j))
                    stuck.add(str(i) + "_" + str(j + 1))
                if j == 0 and grid[i][j] == -1:
                    stuck.add(str(i) + "_" + "0")
                if j == len(grid[0]) - 1 and grid[i][j] == 1:
                    stuck.add(str(i) + "_" + str(len(grid[0]) - 1))
        res = [0 for _ in range(len(grid[0]))]
        for j in range(len(grid[0])):
            for i in range(len(grid)):
                if i == 0:
                    curr = grid[0][j]