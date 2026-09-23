# -*- coding: utf-8 -*-
"""
Problem Description:
You are planning an overnight hike with designated campsites.
You are given a non-decreasing integer array L of length n, where L[i] (0-indexed)
is the cumulative hours required to hike from the trailhead to campsite i.
The last element L[n-1] is the destination. Each day you may hike forward to any
later campsite and stop there.

Given an integer m (max number of days/stops you're allowed to use, excluding
the final destination day), return the minimum possible value of the longest single
day hiking time that allows you to finish the trail using at most m + 1 days.

Formally, partition the journey into at most m + 1 consecutive segments along L
(from 0 hours to L[n-1]), and minimize the maximum segment length. A segment from
campsite i to campsite j (i < j) takes L[j] - L[i] hours on that day.

Example:
L = [2, 5, 10], m = 1
valid_hike_options = [[2, 8], [10], [5, 5]]
output: 5
Explanation: Make one stop at campsite 1 (cumulative 5 hours). Segments are [5, 5]. max([5, 5]) -> 5.
"""

class Solution(object):
    def minMaxHikingTime(self, L, m):
        # 1. 还原出每一段的实际距离 nums
        nums = []
        prev = 0
        for x in L:
            nums.append(x - prev)
            prev = x

        # 2. 贪心验证函数：如果每天最多走 max_hours，需要扎营几次？
        def canFinish(max_hours):
            camps = 0
            curr_day_hours = 0
            for distance in nums:
                if curr_day_hours + distance > max_hours:
                    # 今天走不到了，必须扎营休息，把这段路留到明天
                    camps += 1
                    curr_day_hours = distance
                else:
                    # 今天还能继续走
                    curr_day_hours += distance
            return camps <= m

        # 3. 二分查找答案 (Binary Search on Answer)
        left = max(nums)  # 答案的下界：最少也要走最长的那一段
        right = L[-1]     # 答案的上界：最多就是一天走完全程

        while left < right:
            mid = (left + right) / 2
            if canFinish(mid):
                # 能在这个强度下走完，说明 mid 可能是答案，或者可以尝试更轻松的强度（缩小上限）
                right = mid
            else:
                # 这个强度走不完（需要的扎营次数 > m），说明每天必须多走一点（提高下限）
                left = mid + 1

        return left

# ================= 测试代码 =================
if __name__ == "__main__":
    sol = Solution()

    L = [2, 5, 10]
    m = 1
    # 期望输出: 5
    print "Output for L=[2,5,10], m=1:", sol.minMaxHikingTime(L, m)

    # 额外测试用例：如果不扎营 (m=0)
    print "Output for L=[2,5,10], m=0:", sol.minMaxHikingTime(L, 0) # 应该输出 10