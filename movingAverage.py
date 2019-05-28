# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
#
# For example,
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3
import collections
class Solution(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.maxsize = size
        self.sum = 0
        self.window = collections.deque()

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.window.append(val)
        if len(self.window) < self.maxsize:
            self.sum += val
        else:
            self.sum += val - self.window.popleft()

        return self.sum / self.maxsize