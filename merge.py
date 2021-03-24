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

    # Microsoft onsite, merge one new interval into sorted intervals
    # LC 57 Insert Interval, checkout insert.py
    def mergeNew(self, intervals, newInterval):
        arr = []
        isMerged = False
        # try to merge conflict
        for interval in intervals:
            if not isMerged:
                st = max(interval.start, newInterval.start)
                ed = min(interval.end, newInterval.end)
                if st >= ed:
                    arr.append(min(interval.start, newInterval.start), max(interval.end, newInterval.end))
                    isMerged = True
                else:
                    arr.append(interval)
            # resolve remaining possible conflict
            else:
                if arr[-1].end < interval.start:
                    arr.append(interval)
                else:
                    arr[-1].end = max(arr[-1].end, interval.end)
        res = []
        if isMerged:
            return arr
        # handle no conflict at all, insert in between
        else:
            for i in range(len(arr) - 1):
                if arr[i].end < newInterval.start and arr[i + 1].start > newInterval.end:
                    res.append(arr[i])
                    res.append(newInterval)
                    isMerged = True
                else:
                    res.append(arr[i])
            res.append(arr[-1])
        # no conflict and at before head or after tail
        if not isMerged:
            if newInterval.start > res[-1].end:
                res.append(newInterval)
            elif newInterval.end < res[0].start:
                res = [newInterval] + res
        return res

test = Solution()
# print test.merge([[1,3],[2,6],[8,10],[15,18]])