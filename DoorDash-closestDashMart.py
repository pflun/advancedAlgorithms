# A DashMart is a warehouse run by DoorDash that houses items found in
# convenience stores, grocery stores, and restaurants. We have a city with open
# roads, blocked-off roads, and DashMarts.
# City planners want you to identify how far a location is from its closest
# DashMart.
# Locations are given in [row, col] format.
# Example:
# [
# # 0 1 2 3 4 5 6 7 8
# ['X', ' ', ' ', 'D', ' ', ' ', 'X', ' ', 'X'], # 0
# ['X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', 'X'], # 1
# [' ', ' ', ' ', 'D', 'X', 'X', ' ', 'X', ' '], # 2
# [' ', ' ', ' ', 'D', ' ', 'X', ' ', ' ', ' '], # 3
# [' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X'], # 4
# [' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X', 'X'] # 5
# ]
# ' ' represents an open road that you can travel over in any direction (up, down, left, or right).
# 'X' represents an blocked road that you cannot travel through.
# 'D' represents a DashMart.
# # list of pairs [row, col]
# locations = [
# [2, 2],
# [4, 0],
# [0, 4],
# [2, 6],
# ]
# answer = [1, 4, 1, 5]

class Solution(object):
    def closestDashMart(self, city, locations):

        def bfs(x, y):
            dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            visited = set((x, y))
            queue = [[x, y]]
            steps = 1
            while queue:
                size = len(queue)
                for _ in range(size):
                    curr = queue.pop(0)
                    for d in dir:
                        currx = curr[0] + d[0]
                        curry = curr[1] + d[1]
                        if currx < 0 or currx == len(city[0]) or curry < 0 or curry == len(city) or (currx, curry) in visited or city[curry][currx] == 'X':
                            continue
                        if city[curry][currx] == ' ':
                            city[curry][currx] = steps
                        elif type(city[curry][currx]) == int:
                            city[curry][currx] = min(city[curry][currx], steps)
                        visited.add((currx, curry))
                        queue.append([currx, curry])
                steps += 1

            return

        # from each DashMart bfs update each empty cell with shortest distance
        for j in range(len(city)):
            for i in range(len(city[0])):
                if city[j][i] == 'D':
                    bfs(i, j)
        res = []
        for l in locations:
            res.append(city[l[0]][l[1]])
        return res

test = Solution()
print test.closestDashMart([
['X', ' ', ' ', 'D', ' ', ' ', 'X', ' ', 'X'],
['X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', 'X'],
[' ', ' ', ' ', 'D', 'X', 'X', ' ', 'X', ' '],
[' ', ' ', ' ', 'D', ' ', 'X', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X'],
[' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X', 'X']
], [
[2, 2],
[4, 0],
[0, 4],
[2, 6],
])
