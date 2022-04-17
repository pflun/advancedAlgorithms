# -*- coding: utf-8 -*-
# 找到k个距离餐馆最近的送餐员 如果距离相同 就比评分
# points 0, 1 是坐标，2是评分
import heapq
class Solution(object):
    def kClosest(self, points, k):
        arr = [[x[0] * x[0] + x[1] * x[1], x[2]] for x in points]

        def sort_func(distance, score):
            return (
                distance,
                score
            )

        arr.sort(key=lambda a: sort_func(a[0], -a[1]), reverse=False)

        # arr miss了坐标，加上放后面就行
        return arr[:k]

    # 用最大heap
    # heap用tuple as comparator, 另外py2用__cmp__也可以
    def kClosest2(self, points, k):
        heap = []
        heapq.heapify(heap)
        for x in points:
            if len(heap) < k:
                heapq.heappush(heap, (-x[0] * x[0] - x[1] * x[1], x[2]))
            else:
                heapq.heappushpop(heap, (-x[0] * x[0] - x[1] * x[1], x[2]))
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap))
        return res

test = Solution()
print test.kClosest2([[1,1,7],[-2,2,8],[2,2,9]], 2)