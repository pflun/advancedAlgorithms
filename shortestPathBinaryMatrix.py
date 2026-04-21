class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1

        self.dir = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        step = 0
        queue = [[0, 0]]
        visited = set()
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                visited.add((curr[0], curr[1]))
                if curr[0] == len(grid) - 1 and curr[1] == len(grid[0]) - 1:
                    return step + 1
                for d in self.dir:
                    currx = curr[0] + d[0]
                    curry = curr[1] + d[1]
                    if currx < 0 or currx == len(grid) or curry < 0 or curry == len(grid[0]) or (currx, curry) in visited or grid[currx][curry] != 0:
                        continue
                    queue.append([currx, curry])
            step += 1
        return -1

test = Solution()
print test.shortestPathBinaryMatrix([[0,1],[1,0]])
print test.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]])
print test.shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]])