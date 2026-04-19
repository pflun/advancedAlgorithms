# -*- coding: utf-8 -*-
# 给了几个大巴线路时刻表，有每站之间行驶时间，等待时间。
# 输入是（地点1，地点2，出发时间）
# 输出是 最早到达时间
import heapq

class Solution(object):
    def earliestArrivalTime(self, times, n, k, start_time, target):
        # times 结构假设为: (起点, 终点, 离开时间, 到达时间)
        adj = {i: [] for i in range(1, n + 1)}
        for u, v, dep, arr in times:
            adj[u].append((dep, arr, v))

        # 对每个站点的班次按出发时间排序，方便二分查找或线性查找
        for u in adj:
            adj[u].sort()

        # heap 存储: (当前到达时间, 当前站点)
        heap = [(start_time, k)]
        # visited 记录到达每个站点的最早时间
        earliest = {}

        while heap:
            time, u = heapq.heappop(heap)

            if u in earliest:
                continue
            earliest[u] = time

            if u == target:
                return time

            if u in adj:
                for dep, arr, v in adj[u]:
                    # 核心改变：只有出发时间 >= 我到达当前站的时间，我才能坐这班车
                    if dep >= time:
                        # 如果之前还没到过 v，或者这班车能更早到 v
                        if v not in earliest:
                            heapq.heappush(heap, (arr, v))
                            # 注意：这里不能像传统 Dijkstra 一样立即 break
                            # 因为后边的班次虽然出发晚，但可能到达更早（虽然在大巴场景少见）
                            # 但为了严谨，我们通常按到达时间 pop

        return earliest.get(target, -1)

# 假设时间单位为整数（例如表示几点钟）
times = [
        # (起点, 终点, 出发时间, 到达时间)
        (1, 2, 0, 10),   # 路线A：1直达2。10点才到。
        (1, 3, 2, 5),    # 路线B：先去3。5点到。
        (3, 2, 6, 9),    # 路线B：从3转车去2。9点就到了！（比直达还快）
        (2, 4, 9, 15),   # 去终点4的早班车：9点发车，15点到。
        (2, 4, 12, 20)   # 去终点4的晚班车：12点发车，20点到。
    ]

n = 4           # 总共有 4 个城市
k = 1           # 起点是 1
target = 4      # 终点是 4
start_time = 0  # 我们的出发时间是 0
test = Solution()
print test.earliestArrivalTime(times, n, k, start_time, target) # 15