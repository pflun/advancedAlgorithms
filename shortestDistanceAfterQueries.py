# If not using cache, TLE at n = 500
import heapq
class Solution(object):
    def shortestDistanceAfterQueries(self, n, queries):
        res = []
        graph = {}
        for i in range(n - 1):
            graph[i] = {i + 1: 1}
        for q in queries:
            graph[q[0]][q[1]] = 1
            distance = self.dijkstra(graph, 0, n - 1, n)
            res.append(distance)
        return res

    def dijkstra(self, graph, start, end, n):
        cache = [float('inf')] * n
        cache[0] = 0
        heap = [(0, start)]
        heapq.heapify(heap)
        while heap:
            distance, city = heapq.heappop(heap)
            if city == end:
                return distance
            # use cache to prune
            if distance > cache[city]:
                continue
            if city in graph:
                for next_city in graph[city].keys():
                    # use cache to prune and update cache
                    if distance + graph[city][next_city] < cache[next_city]:
                        cache[next_city] = distance + graph[city][next_city]
                        heapq.heappush(heap, (distance + graph[city][next_city], next_city))
        return end

test = Solution()
print test.shortestDistanceAfterQueries(5, [[2,4],[0,2],[0,4]])
print test.shortestDistanceAfterQueries(4, [[0,3],[0,2]])