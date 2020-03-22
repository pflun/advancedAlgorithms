# -*- coding: utf-8 -*-
# 下面code是contest时写的比较乱，这题bfs(queue)和dfs都行，我当时写得比较乱是因为我对每个cell的状态做检查(比如1不能和2相连)
# 实际上可以做一个状态=>position的map，如下所示，状态1只能走到左边那格和右边那格
# directions = {1: [(0,-1),(0,1)],
#               2: [(-1,0),(1,0)],
#               3: [(0,-1),(1,0)],
#               4: [(0,1),(1,0)],
#               5: [(0,-1),(-1,0)],
#               6: [(0,1),(-1,0)]}
# 用一个visited保证不往回走减少计算量，毕竟是双向走动
class Solution(object):
    def hasValidPath(self, grid):
        self.valid = {1:[1, 3, 4, 5, 6], 2: [2, 3, 4, 5, 6], 3: [1, 2, 4, 5, 6], 4:[1, 2, 3, 5, 6], 5:[1, 2, 3, 4, 6], 6:[1, 2, 3, 4, 5]}
        self.found = False
        self.res = False
        def dfs(grid, px, py, cx, cy):
            if self.found:
                return
            if cx < 0 or cy < 0 or cx == len(grid) or cy == len(grid[0]):
                return
            next = grid[cx][cy]
            prev = grid[px][py]
            if next not in self.valid[prev]:
                return
            else:
                if cx == len(grid) - 1 and cy == len(grid[0]) - 1:
                    self.found = True
                    self.res = True
                    return
                if next == 1:
                    if py == cy - 1:
                        dfs(grid, cx, cy, cx, cy + 1)
                    elif py == cy + 1:
                        dfs(grid, cx, cy, cx, cy - 1)
                elif next == 2:
                    if px == cx - 1:
                        dfs(grid, cx, cy, cx + 1, cy)
                    elif px == cx + 1:
                        dfs(grid, cx, cy, cx - 1, cy)
                elif next == 3:
                    if py == cy - 1:
                        dfs(grid, cx, cy, cx + 1, cy)
                    elif px == cx + 1:
                        dfs(grid, cx, cy, cx, cy - 1)
                elif next == 4:
                    if py == cy + 1:
                        dfs(grid, cx, cy, cx + 1, cy)
                    elif px == cx + 1:
                        dfs(grid, cx, cy, cx, cy + 1)
                elif next == 5:
                    if py == cy - 1:
                        dfs(grid, cx, cy, cx - 1, cy)
                    elif px == cx - 1:
                        dfs(grid, cx, cy, cx, cy - 1)
                elif next == 6:
                    if py == cy + 1:
                        dfs(grid, cx, cy, cx - 1, cy)
                    elif px == cx - 1:
                        dfs(grid, cx, cy, cx, cy + 1)

        if grid[0][0] == 1 or grid[0][0] == 6:
            dfs(grid, 0, 0, 0, 1)
        elif grid[0][0] == 2 or grid[0][0] == 3:
            dfs(grid, 0, 0, 1, 0)
        return self.found

test = Solution()
print test.hasValidPath([[2,4,3],[6,5,2]])
print test.hasValidPath([[1,2,1],[1,2,1]])
print test.hasValidPath([[1,1,2]])
print test.hasValidPath([[1,1,1,1,1,1,3]])
print test.hasValidPath([[2],[2],[2],[2],[2],[2],[6]])
