class Solution(object):
    def wallsAndGates(self, rooms):
        queue = []
        # push all 0s (gates)
        for y in range(len(rooms)):
            for x in range(len(rooms[0])):
                if rooms[y][x] == 0:
                    queue.append((y, x))

        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        while queue:
            y, x = queue.pop(0)
            for d in dir:
                ny = y + d[0]
                nx = x + d[1]
                # out of border or distance to another gate smaller than this gate
                if ny < 0 or ny >= len(rooms) or nx < 0 or nx >= len(rooms[0]) or rooms[ny][nx] < rooms[y][x] + 1:
                    continue
                # found shorter distance, then update
                rooms[ny][nx] = rooms[y][x] + 1
                queue.append((ny, nx))

        return rooms