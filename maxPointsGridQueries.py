# -*- coding: utf-8 -*-
# https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/
# Return answer, answer[i] is the maximum number of points you can get.
class Solution(object):
    # TLE
    def maxPoints(self, grid, queries):
        self.res = []
        self.dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for q in queries:
            if grid[0][0] > q:
                self.res.append(0)
                continue
            points = self.bfs(grid, q)
            self.res.append(points)

        return self.res

    def bfs(self, grid, q):
        queue = [[0, 0]]
        visited = set()
        while queue:
            curr = queue.pop(0)
            visited.add((curr[0], curr[1]))
            for d in self.dir:
                currx = curr[0] + d[0]
                curry = curr[1] + d[1]
                if currx < 0 or currx == len(grid) or curry < 0 or curry == len(grid[0]) or (currx, curry) in visited or grid[currx][curry] >= q:
                    continue
                queue.append([currx, curry])
        return len(visited)

test = Solution()
print test.maxPoints([[1,2,3],[2,5,7],[3,5,1]], [5,6,2])
print test.maxPoints([[5,2,1],[1,1,2]], [3])

# Heap + don't empty visited + BFS
# 第一步：整理 Queries
# 原来的 queries: [5, 6, 2]
# 排序后并带上原始索引: [(2, 原始索引2), (5, 原始索引0), (6, 原始索引1)]
#
# 第二步：初始化
# * 最小堆 heap = [(1, x=0, y=0)] (存入起始点，按高度 1 排序)
# * visited = {(0,0)}
# * 当前能到达的格子总数 count = 0
# * 结果数组 res = [0, 0, 0]
#
# 第三步：开始按水位上涨模拟
#
# 🌊 水位 q = 2 (原始索引 2)
# 我们看向堆顶：当前最矮的格子是 (0,0)，高度为 1。
# * 1 < 2，水可以淹没它！
# * 弹出 (1, 0, 0)，总数 count += 1（此时 count=1）。
# * 把它的邻居加入堆：右边高度 2，下边高度 2。
# * 此时 heap = [(2, 0,1), (2, 1,0)]。
#
# 接着看堆顶：高度 2。
# * 2 >= 2，水被挡住了，淹不过去了。
# * 结算：水位为 2 时的答案就是当前的 count，即 1。
# * 记录答案：res[原始索引2] = 1。
#
# 🌊 水位 q = 5 (原始索引 0)
# 注意！我们不需要清空堆和 visited，直接继续！
# 当前 heap = [(2, 0,1), (2, 1,0)]，count = 1。
#
# 看堆顶，高度 2。
# * 2 < 5，水可以突破！
# * 弹出 (2, 0,1)，count += 1 (变 2)。加邻居：(0,2)高3，(1,1)高5。
# * 弹出 (2, 1,0)，count += 1 (变 3)。加邻居：(2,0)高3。
# * 此时堆里最矮的是高度 3。3 < 5，继续突破！
# * 弹出 (3, 0,2)，count += 1 (变 4)。加邻居：(1,2)高7。
# * 弹出 (3, 2,0)，count += 1 (变 5)。加邻居：(2,1)高5。
#
# 此时 heap = [(5, 1,1), (5, 2,1), (7, 1,2)]。
# 看堆顶：高度 5。
# * 5 >= 5，水又被挡住了。
# * 结算：水位为 5 时的答案就是当前的 count，即 5。
# * 记录答案：res[原始索引0] = 5。
#
# 🌊 水位 q = 6 (原始索引 1)
# 继续沿用当前状态：heap = [(5, 1,1), (5, 2,1), (7, 1,2)]，count = 5。
#
# 看堆顶，高度 5。
# * 5 < 6，突破！
# * 弹出 (5, 1,1)，count += 1 (变 6)。没有新邻居可加。
# * 弹出 (5, 2,1)，count += 1 (变 7)。加邻居：(2,2)高1。
# * 此时堆里冒出来一个极低的洼地！heap = [(1, 2,2), (7, 1,2)]。
# * 1 < 6，必须淹没！弹出 (1, 2,2)，count += 1 (变 8)。
#
# 此时 heap = [(7, 1,2)]。
# 看堆顶，高度 7。
# * 7 >= 6，水最终被挡住了。
# * 结算：水位为 6 时的答案是 count，即 8。
# * 记录答案：res[原始索引1] = 8。
#
# 最终结果组装：
# res = [5, 8, 1]。这完美匹配了你跑出来的正确答案！全程网格只遍历了 1次，性能有了质的飞跃。