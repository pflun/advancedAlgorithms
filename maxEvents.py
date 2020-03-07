# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=NjF9JGDGxg8
# 按结束时间排序
class Solution(object):
    def maxEvents(self, events):
        events = sorted(events, key=lambda x: x[1])
        res = 0
        used = [False for _ in range(10001)]

        for e in events:
            for i in range(e[0], e[1] + 1):
                if used[i]:
                    continue
                used[i] = True
                res += 1
                break
        return res

test = Solution()
print test.maxEvents([[1,4],[4,4],[2,2],[3,4],[1,1]])
print test.maxEvents([[1,2],[2,3],[3,4]])
print test.maxEvents([[1,2],[2,3],[3,4],[1,2]])