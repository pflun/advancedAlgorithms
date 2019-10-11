class Solution(object):
    def getMaximumGold(self, grid):
        if len(grid) == 0:
            return
        self.res = 0
        self.dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    self.res = max(self.res, self.dfs(grid, i, j, set(), 0))
        return self.res

    def dfs(self, grid, i, j, visited, gold):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] == 0 or (i, j) in visited:
            return gold
        visited.add((i, j))
        gold += grid[i][j]
        tmpGold = 0
        for d in self.dir:
            x = i + d[0]
            y = j + d[1]
            tmpGold = max(tmpGold, self.dfs(grid, x, y, visited, gold))
        visited.remove((i, j))
        return tmpGold

test = Solution()
print test.getMaximumGold([
    [1,0,7],
    [2,0,6],
    [3,4,5],
    [0,3,0],
    [9,0,20]])
print test.getMaximumGold([
    [0,0,0,0,0,0,32,0,0,20],
    [0,0,2,0,0,0,0,40,0,32],
    [13,20,36,0,0,0,20,0,0,0],
    [0,31,27,0,19,0,0,25,18,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,18,0,6],
    [0,0,0,25,0,0,0,0,0,0],
    [0,0,0,21,0,30,0,0,0,0],
    [19,10,0,0,34,0,2,0,0,27],[0,0,0,0,0,34,0,0,0,0]])