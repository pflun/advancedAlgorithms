# -*- coding: utf-8 -*-
# Graph DFS + heap
# 代码中heap里直接是node，我们也可以 heapq.heappush([rating, node])
import heapq

class Movie(object):
    def __init__(self, id, rating):
        self.movieId = id
        self.rating = rating
        self.similarMovies = []

    def getId(self):
        return self.movieId

    def getRating(self):
        return self.rating

    def addSimilarMovie(self, movie):
        self.similarMovies.append(movie)

    def getSimilarMovies(self):
        return self.similarMovies

class Solution(object):
    def getNearestMovies(self, movie, N):
        res = []
        if not movie:
            return res
        heap = []
        visited = set()
        visited.add(movie)

        # 对于每个相似movie dfs
        for m in movie.similarMovies:
            self.dfs(m, N, heap, visited)

        # 剩下size为 N 的 heap 全部加入res
        while heap:
            res = [heapq.heappop(heap)] + res

        return res

    def dfs(self, m, N, heap, visited):
        if m in visited:
            return
        # 访问过了
        visited.add(m)
        # 与堆顶比较rating
        if len(heap) == N:
            if m.rating > heap[0].rating:
                heapq.heappop(heap)
                heapq.heappush(heap, m)
        else:
            heapq.heappush(heap, m)

        # 对于当前movie相似的那些，继续dfs，退出条件就是visited
        for mv in m.similarMovies:
            self.dfs(mv, N, heap, visited)

movie1 = Movie(1, 1.2)
movie2 = Movie(2, 3.6)
movie3 = Movie(3, 2.4)
movie4 = Movie(4, 4.8)
movie1.addSimilarMovie(movie2)
movie1.addSimilarMovie(movie3)
movie2.addSimilarMovie(movie4)
movie3.addSimilarMovie(movie4)
# print movie1.getSimilarMovies()[0].movieId
test1 = Solution()
print test1.getNearestMovies(movie1, 2)[1].movieId