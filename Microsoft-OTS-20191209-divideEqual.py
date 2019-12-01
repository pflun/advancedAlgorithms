# -*- coding: utf-8 -*-
# 给你一个sorted array， 和一个integer n表示numbers of buckets，
#    写一个function把这个sorted array 分解成n个sub array，
#    使得每个sub array 的总和（weights） 差不多相同。 （approximately equals）
# EX: [1,2,3,4,5], result = [[5], [4,1],[3,2]]
# heap存[tmp_sum, 当前bucket的元素], 从大到小排序遍历，heap size不够n就新建bucket，够了n就加入heap顶(最小bucket)
import heapq
class Solution(object):
    def divideEqual(self, arr, n):
        heap = []
        heapq.heapify(heap)
        # 题目是排序好的，所以反过来就行，否则要排序reverse=True
        for a in arr[::-1]:
            if len(heap) < n:
                heapq.heappush(heap, [a, [a]])
            else:
                curr = heapq.heappop(heap)
                curr[0] += a
                curr[1].append(a)
                heapq.heappush(heap, curr)
        res = []
        while heap:
            curr = heapq.heappop(heap)
            res.append(curr[1])
        return res

test = Solution()
print test.divideEqual([1,2,3,4,5], 3)