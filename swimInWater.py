# -*- coding: utf-8 -*-
# We can binary search the minimum t (time) such that you can reach the end:
# For a given t, check if there exists a path from start to end where all cells ≤ t.
# If reachable → try smaller t.
# Else → increase t.
class Solution(object):
    def swimInWater(self, grid):
        self.dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # Reachable, no need backtracking
        def dfs(grid, i, j, visited, time):
            if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]) or (i, j) in visited or grid[i][j] > time:
                return
            visited.add((i, j))
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                self.found = True
                return
            for d in self.dir:
                x = i + d[0]
                y = j + d[1]
                dfs(grid, x, y, visited, time)

        l, r = 0, len(grid) * len(grid)
        while l < r:
            m = (l + r) / 2
            self.found = False
            dfs(grid, 0, 0, set(), m)
            if self.found:
                r = m
            else:
                l = m + 1
        # 找到最小的l，使得dfs()为True
        return l

test = Solution()
print test.swimInWater([
    [0,1,2,3,4],
    [24,23,22,21,5],
    [12,13,14,15,16],
    [11,17,18,19,20],
    [10,9,8,7,6]])
print test.swimInWater([[35,19,17,25,4,10],[8,18,29,21,28,31],[15,5,33,2,13,3],[26,20,27,23,11,1],[6,14,24,7,12,16],[30,34,32,22,0,9]])