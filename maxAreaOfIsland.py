class Solution(object):
    # DFS
    def maxAreaOfIsland(self, grid):
        res = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    visited = set()
                    self.size = 0
                    self.dfs(grid, i, j, visited)
                    res = max(res, self.size)

        return res

    def dfs(self, grid, i, j, visited):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or (i, j) in visited or grid[i][j] != 1:
            return

        visited.add((i, j))
        self.size += 1
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for d in dir:
            currx = i + d[0]
            curry = j + d[1]
            self.dfs(grid, currx, curry, visited)

    # BFS
    def maxAreaOfIsland2(self, grid):
        self.visited = set()
        self.res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in self.visited:
                    self.res = max(self.res, self.bfs(grid, i, j))
        return self.res

    def bfs(self, grid, i, j):
        res = 0
        queue = [[i, j]]
        while queue:
            res += 1
            curr = queue.pop(0)
            x, y = curr[0], curr[1]
            self.visited.add((x, y))
            for d in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nx = x + d[0]
                ny = y + d[1]
                if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or (nx, ny) in self.visited or grid[nx][ny] != 1:
                    continue
                queue.append([nx, ny])
        return res

test = Solution()
print test.maxAreaOfIsland([
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]])
