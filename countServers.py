class Solution(object):
    def countServers(self, grid):
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and self.isValid(grid, i, j):
                    res += 1
        return res

    def isValid(self, grid, i, j):
        for x in range(len(grid)):
            if x != i and grid[x][j] == 1:
                return True
        for y in range(len(grid[0])):
            if y != j and grid[i][y] == 1:
                return True
        return False

test = Solution()
print test.countServers([[1,0],[0,1]])
print test.countServers([[1,0],[1,1]])
print test.countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]])