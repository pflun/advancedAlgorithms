import heapq


class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.large = []
        heapq.heapify(self.small)
        heapq.heapify(self.large)
        self.odd = False

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        self.odd = not self.odd
        if self.odd:
            if self.large and num < self.large[0]:
                heapq.heappush(self.small, -num)
            elif self.large and num > self.large[0]:
                tmp = heapq.heappop(self.large)
                heapq.heappush(self.large, num)
                heapq.heappush(self.small, -tmp)
            elif len(self.large) == 0:
                heapq.heappush(self.small, -num)
        else:
            if len(self.large) == 0:
                heapq.heappush(self.large, num)
            elif self.small and num > -self.small[0]:
                heapq.heappush(self.large, num)
            elif self.small and num < -self.small[0]:
                tmp = -heapq.heappop(self.small)
                heapq.heappush(self.large, tmp)
                heapq.heappush(self.small, -num)

        print self.small, self.large

    def findMedian(self):
        """
        :rtype: float
        """
        if self.odd:
            return -self.small[0]
        else:
            print 3.0 / 2
            return (round(-self.small[0] + self.large[0], 1)) / 2

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        inDegree = {}

        for course in prerequisites:
            inDegree[course[0]] = inDegree.get(course[0], 0) + 1

        return inDegree


obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
obj.addNum(4)
obj.addNum(3)
print obj.findMedian()
print obj.canFinish(3, [[1,0],[1, 2],[2,0]])
print sorted('tea')