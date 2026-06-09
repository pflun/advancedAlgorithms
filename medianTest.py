# -*- coding: utf-8 -*-
import heapq

class MedianFinder(object):
    def __init__(self):
        self.small = []  # 最大堆 (存较小的一半，用负数模拟)
        self.large = []  # 最小堆 (存较大的一半)

    def addNum(self, num):
        if len(self.small) == 0 or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)

        self._balance()

    def deleteNum(self, num):
        """
        简单易懂的 O(N) 删除法
        """
        # 1. 判断数字在哪个堆里，并删除
        if len(self.small) > 0 and num <= -self.small[0]:
            # 注意 small 里存的是负数
            if -num in self.small:
                self.small.remove(-num)
                heapq.heapify(self.small) # 删除破坏了堆结构，重新建堆 O(N)
        else:
            if num in self.large:
                self.large.remove(num)
                heapq.heapify(self.large) # 重新建堆 O(N)
                
        # 2. 删除后可能会导致两个堆严重不平衡，需要重新平衡
        self._balance()

    def findMedian(self):
        # 根据两个堆的长度动态判断奇偶，不要用 self.odd
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return float(self.large[0])
        else:
            # 长度相等，取两个堆顶的平均值
            return (-self.small[0] + self.large[0]) / 2.0

    def _balance(self):
        """
        辅助函数：确保 small 的长度 == large 的长度，或者 small 比 large 多 1
        """
        if len(self.small) > len(self.large) + 1:
            tmp = -heapq.heappop(self.small)
            heapq.heappush(self.large, tmp)
        elif len(self.large) > len(self.small):
            tmp = heapq.heappop(self.large)
            heapq.heappush(self.small, -tmp)

# 测试代码
if __name__ == "__main__":
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    obj.addNum(3)
    print "Added 1, 2, 3 -> Median:", obj.findMedian() # 预期 2

    obj.deleteNum(2)
    print "Deleted 2 -> Median:", obj.findMedian()     # 预期 (1+3)/2 = 2.0

    obj.addNum(5)
    print "Added 5 -> Median:", obj.findMedian()       # 现有 1, 3, 5，预期 3

    obj.deleteNum(1)
    print "Deleted 1 -> Median:", obj.findMedian()     # 现有 3, 5，预期 4.0
