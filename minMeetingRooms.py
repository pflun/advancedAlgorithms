# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=0roQnDBC27o
# 一间屋子，有人进有人出，某一时刻最大人数与具体谁几点进出无关
class Solution(object):
    def minMeetingRooms(self, intervals):
        starts = []
        ends = []
        res = 0

        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)

        starts.sort()
        ends.sort()
        print starts, ends

        i = 0
        j = 0
        curr = 0
        # curr：某一时刻屋里一共几个人
        while i < len(intervals):
            # 双指针，i进人，j出人
            if starts[i] < ends[j]:
                curr += 1
                res = max(res, curr)
                i += 1
            elif starts[i] > ends[j]:
                curr -= 1
                j += 1
            else:
                i += 1
                j += 1

        return res


test = Solution()
# print test.minMeetingRooms([[0, 30],[5, 15],[15, 20]])
