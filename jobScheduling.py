# -*- coding: utf-8 -*-
# 变种背包问题：dp[time][profit] 到time能获得的最大收益（time这一点不一定被占用）
# 对于i，不做收益就是dp[-1][1]，做就找i时间点前profit最大的（i就是当前job的start）
# 最一开始按照endTime排序
class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp = [[0, 0]]
        for s, e, p in jobs:
            i = bisect.bisect(dp, [s + 1]) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]