# -*- coding: utf-8 -*-
# https://leetcode.com/problems/as-far-from-land-as-possible/
# 1162. As Far from Land as Possible
import heapq
class Solution(object):
    # TLE
    def maxDistance(self, grid):
        lands = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    lands.append([i, j])
        if not lands:
            return -1
        heap = []
        heapq.heapify(heap)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    tmp = float('inf')
                    for l in lands:
                        tmp = min(tmp, self.manhattanDistance([i, j], l))
                    heapq.heappush(heap, -tmp)
        return -heapq.heappop(heap) if heap else -1

    def manhattanDistance(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    # 对于每个land bfs，找最远的water，直到queue empty
    # BFS找最短：找到第一个就返回
    # 找最长：往queue里加available路径，直到queue empty
    def maxDistance2(self, grid):
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue.append((i, j))
        if len(queue) == 0 or len(queue) == len(grid) * len(grid[0]):
            return -1
        distance = -1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            distance += 1
            for _ in range(len(queue)):
                curr = queue.pop(0)
                for d in directions:
                    currx = curr[0] + d[0]
                    curry = curr[1] + d[1]
                    if 0 <= currx < len(grid) and 0 <= curry < len(grid[0]) and grid[currx][curry] == 0:
                        grid[currx][curry] = 2
                        queue.append((currx, curry))
        return distance

test = Solution()
print test.maxDistance2([[1,0,1],[0,0,0],[1,0,1]])
print test.maxDistance2([[1,0,0],[0,0,0],[0,0,0]])
print test.maxDistance2([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
print test.maxDistance2([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]])