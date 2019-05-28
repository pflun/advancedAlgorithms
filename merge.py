# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        res = []
        intervals = sorted(intervals, key=lambda x: x.start)
        for interval in intervals:
            # first interval or no overlap
            if len(res) == 0 or res[-1].end < interval.start:
                res.append(interval)
            else:
                # update last interval
                res[-1].end = max(res[-1].end, interval.end)

        return res

test = Solution()
# print test.merge([[1,3],[2,6],[8,10],[15,18]])