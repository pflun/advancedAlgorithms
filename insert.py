# -*- coding: utf-8 -*-
# Assume sorted, intervals = sorted(intervals, key=lambda x: x.start)
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        res = []
        res.append(intervals[0])

        for interval in intervals[1:]:
            # 外层if是 Merge Interval，用来处理把newInterval加进去以后的情况
            if res[-1].end < interval.start:
                # interval 和 newInterval 无交集
                if interval.end < newInterval.start:
                    res.append(interval)
                # 有交集
                else:
                    # 把interval.end 更新成 newInterval.end 再加进res，然后剩下的按照 Merge Interval 处理
                    if interval.end < newInterval.end:
                        interval.end = newInterval.end
                    res.append(interval)
            else:
                res[-1].end = max(res[-1].end, interval.end)

        return res

test = Solution()
print test.insert([Interval(1, 2), Interval(3, 5), Interval(6, 7), Interval(8, 10), Interval(12, 16)], Interval(4, 9))