# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        # Same: intervals = sorted(intervals, key=lambda x:x.start)
        intervals.sort(key=lambda x: x.start)

        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False

        return True

m1 = Interval(0, 5)
m2 = Interval(5, 10)
m3 = Interval(15, 20)

test = Solution()
print test.canAttendMeetings([m1, m2, m3])