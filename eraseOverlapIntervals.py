# -*- coding: utf-8 -*-
# Greedy: 每次选最早end的，因为可以给以后提更大non conflict空间
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        end, cnt = float('-inf'), 0
        for s, e in sorted(intervals, key=lambda x: x[1]):
            if s >= end:
                end = e
            else:
                cnt += 1
        return cnt