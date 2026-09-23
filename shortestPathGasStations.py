# https://www.hack2hire.com/question-bank/companies/bloomberg/coding-questions/68dc09c39736cfa4e90623e6/practice?questionId=68dc5856dd5418be11109afb&src=eg1
class Solution(object):
    def shortestPath(self, grid, fuelCapacity):
        start = end = None
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 'S':
                    start = (r, c)
                if grid[r][c] == 'D':
                    end = (r, c)

        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        step = 0
        queue = [[start[0], start[1], fuelCapacity]]
        visited = set()
        visited.add((start[0], start[1], fuelCapacity))
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                if curr[0] == end[0] and curr[1] == end[1]:
                    return step + 1
                for d in dir:
                    currx = curr[0] + d[0]
                    curry = curr[1] + d[1]
                    new_fuel = curr[2] - 1
                    if new_fuel < 0:
                        continue
                    if currx < 0 or currx == len(grid) or curry < 0 or curry == len(grid[0]) or grid[currx][curry] == '#':
                        continue
                    if grid[currx][curry] == 'G':
                        new_fuel = fuelCapacity
                    if (currx, curry, new_fuel) in visited:
                        continue
                    queue.append([currx, curry, new_fuel])
                    visited.add((currx, curry, new_fuel))
            step += 1
        return -1