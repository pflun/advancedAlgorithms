# -*- coding: utf-8 -*-
import heapq
class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.odd = False
        self.small = []
        self.large = []
        heapq.heapify(self.small)
        heapq.heapify(self.large)

    # 先根据大小选择压入left堆／right堆，然后调整堆size（比如左边拿出一个压入右边），保持left堆和right堆size相等或left多一个的状态
    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        # Add to heap accordingly
        if len(self.small) == 0:
            heapq.heappush(self.small, self.negativify(num))
        else:
            if num <= -self.small[0]:
                heapq.heappush(self.small, self.negativify(num))
            else:
                heapq.heappush(self.large, num)

        # Balance left/right
        if len(self.small) > len(self.large) + 1:
            tmp = -heapq.heappop(self.small)
            heapq.heappush(self.large, tmp)
        elif len(self.large) > len(self.small):
            tmp = heapq.heappop(self.large)
            heapq.heappush(self.small, self.negativify(tmp))

        self.odd = not self.odd
        print self.small, self.large, self.odd


    def findMedian(self):
        """
        :rtype: float
        """
        # odd: 返回left heap最大值；even：返回（left最大 ＋ right最小）除以2
        if self.odd:
            return -self.small[0]
        else:
            return (round(-self.small[0] + self.large[0], 1)) / 2

    def negativify(self, n):
        n = -n
        return n



# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
print obj.findMedian()
obj.addNum(2)
print obj.findMedian()
obj.addNum(2)
print obj.findMedian()
obj.addNum(4)
print obj.findMedian()
obj.addNum(5)
print obj.findMedian()