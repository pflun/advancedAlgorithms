# -*- coding: utf-8 -*-
# LC 57 Insert Interval
# 类似Google Rain Water Drop，binary search找left boundary overlap with newInterval and right boundary，overlap还是用max min去找
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

    # 用newInterval把conflict merge了，res不含conflict
    # 最后把newInterval加到相应位置
    def insert2(self, intervals, newInterval):
        if len(intervals) == 0:
            return [newInterval]
        res = []
        i = 0
        while i < len(intervals):
            tmpS = max(intervals[i][0], newInterval[0])
            tmpE = min(intervals[i][1], newInterval[1])
            if tmpS <= tmpE:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            else:
                res.append(intervals[i])
            i += 1
        if not res:
            return [newInterval]
        if newInterval[1] < res[0][0]:
            return [newInterval] + res
        for i in range(len(res) - 1):
            if res[i + 1][0] > newInterval[1] and res[i][1] < newInterval[0]:
                return res[:i + 1] + [newInterval] + res[i + 1:]
        if newInterval[0] > res[-1][1]:
            return res + [newInterval]

test = Solution()
print test.insert([Interval(1, 2), Interval(3, 5), Interval(6, 7), Interval(8, 10), Interval(12, 16)], Interval(4, 9))