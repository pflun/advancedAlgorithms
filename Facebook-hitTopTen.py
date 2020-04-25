# -*- coding: utf-8 -*-
# 第二个题是自己设计个数据结构，里面支持个hit和top的function。hit的时候包括id和数字，
# top的时候要返回之前hit的top10大的数字的id。相同id hit进来的时候把他们相加。
# 下面handle了positive情况，需要clarify负数情况
import heapq
class Solution(object):
    def __init__(self):
        self.dic = {}
        self.heap = []
        heapq.heapify(self.heap)
        self.exists = set()

    def hit(self, id, num):
        self.dic[id] = self.dic.get(id, 0) + num
        if id not in self.exists:
            if len(self.heap) < 10:
                heapq.heappush(self.heap, [self.dic[id], id])
                self.exists.add(id)
            else:
                rt = heapq.heapreplace(self.heap, [self.dic[id], id])[1]
                self.exists.add(id)
                self.exists.remove(rt)
        else:
            tmp = []
            while self.heap[0][1] != id:
                tmp.append(heapq.heappop(self.heap))
            curr = heapq.heappop(self.heap)
            if curr[1] == id:
                heapq.heappush(self.heap, [self.dic[id], id])
            while tmp:
                heapq.heappush(self.heap, tmo.pop())

    def top(self):
        res = list(self.exists)
        return res

test = Solution()
print test.hit(1,1)
print test.hit(2,1)
print test.hit(1,1)
print test.top()