# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/description/
# 1293. Shortest Path in a Grid with Obstacles Elimination
class Solution(object):
    def shortestPath(self, grid, k):
        self.dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        step = 0
        queue = [[0, 0, k]]
        visited = set()
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                visited.add((curr[0], curr[1]))
                eliminate = curr[2]
                if curr[0] == len(grid) - 1 and curr[1] == len(grid[0]) - 1:
                    return step
                for d in self.dir:
                    currx = curr[0] + d[0]
                    curry = curr[1] + d[1]
                    if currx < 0 or currx == len(grid) or curry < 0 or curry == len(grid[0]) or (currx, curry) in visited:
                        continue
                    if grid[currx][curry] == 1 and eliminate == 0:
                        continue
                    remain_eliminate = eliminate - 1 if grid[currx][curry] == 1 else eliminate
                    queue.append([currx, curry, remain_eliminate])
            step += 1
        return -1

test = Solution()
print test.shortestPath([[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], 1)
print test.shortestPath([[0,1,1],[1,1,1],[1,0,0]], 1)