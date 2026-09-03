# -*- coding: utf-8 -*-
class Solution(object):
    def orangesRotting(self, grid):
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        queue = []
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append([i, j])
                elif grid[i][j] == 1:
                    fresh += 1

        step = 0
        while queue and fresh > 0: # fresh=0 就不用继续了，防止多 +1
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                for d in dir:
                    x = curr[0] + d[0]
                    y = curr[1] + d[1]
                    if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and grid[x][y] == 1:
                        grid[x][y] = 2
                        queue.append([x, y])
                        fresh -= 1
            step += 1
        return step if fresh == 0 else -1

test = Solution()
print test.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
print test.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])
print test.orangesRotting([[0,2]])

# What if the time is variable? Some oranges take 1 minute to pop their neighbors, while others take 5 minutes. Use Dijkstra
# BFS 前提是所有边权=1，边权不同时用 Dijkstra min-heap 保证每次处理"当前最早腐烂的橙子"
import heapq

class SolutionVariableRotTimes(object):
    def orangesRottingVariableTimes(self, grid, spread_time):
        rows, cols = len(grid), len(grid[0])

        # dist[r][c] = 这格橙子最早被腐烂的时间（初始 inf）
        dist = [[float('inf')] * cols for _ in range(rows)]
        heap = []   # (time, r, c)
        fresh = 0

        # 多源起点：所有初始腐烂橙子 dist=0 同时入堆
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    dist[r][c] = 0
                    heapq.heappush(heap, (0, r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        while heap:
            time, r, c = heapq.heappop(heap)

            # Dijkstra pop-time 检查：dist 已被更小 time 更新过，这个 entry 过时，跳过
            if time > dist[r][c]:
                continue

            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    # 传染时间 = 当前橙子被腐烂的时间 + 当前橙子自己的传染耗时
                    new_time = time + spread_time[r][c]
                    # Dijkstra relax：只有找到更短路径才更新
                    if new_time < dist[nr][nc]:
                        dist[nr][nc] = new_time
                        heapq.heappush(heap, (new_time, nr, nc))

        # 答案 = 所有新鲜橙子被腐烂的最晚时间（木桶效应）
        result = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    if dist[r][c] == float('inf'):
                        return -1   # 孤立橙子，永远到不了
                    result = max(result, dist[r][c])
        return result

test2 = SolutionVariableRotTimes()
grid1 = [[2,1,1],[1,1,0],[0,1,1]]
st1   = [[1,1,1],[1,1,0],[0,1,1]]   # 所有传染时间=1，结果应和 BFS 一样=4
print test2.orangesRottingVariableTimes(grid1, st1)

grid2 = [[2,1],[1,1]]
st2   = [[5,1],[1,1]]   # 腐烂橙子传染时间=5
# (0,0) t=0 腐烂，spread=5 → (0,1) t=5，(1,0) t=5
# (0,1) spread=1 → (1,1) t=6
# (1,0) spread=1 → (1,1) t=6
# 答案 = 6
print test2.orangesRottingVariableTimes(grid2, st2)  # 6