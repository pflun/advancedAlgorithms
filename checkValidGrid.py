class Solution(object):
    def checkValidGrid(self, grid):
        if grid[0][0] != 0:
            return False
        cnt = 0
        x = 0
        y = 0
        while cnt < len(grid) * len(grid[0]) - 1:
            moves = self.nextMoves(grid, x, y)
            found = False
            for m in moves:
                if grid[m[1]][m[0]] == cnt + 1:
                    x = m[0]
                    y = m[1]
                    cnt += 1
                    found = True
                    break
            if found:
                continue
            else:
                return False
        return True

    def nextMoves(self, grid, x, y):
        res = []
        dirs= [[1, 2], [2, 1], [-1, -2], [-2, -1], [1, -2], [-2, 1], [-1, 2], [2, -1]]
        for d in dirs:
            cx = x + d[0]
            cy = y + d[1]
            if cx >= 0 and cy >= 0 and cx < len(grid) and cy < len(grid[0]):
                res.append([cx, cy])
        return res