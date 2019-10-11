# -*- coding: utf-8 -*-
# 先是要求顺序不能变的，返回执行时间，再是允许变换顺序的，返回最优的排序（原题要求返回最优时间）
class Solution(object):
    # 顺序不变
    def leastInterval(self, tasks, n):
        # res就等于时间线
        res = 0
        # last appear
        last = {}
        for t in tasks:
            if t not in last:
                res += 1
            else:
                lastTime = last[t]
                # 距离上一次执行超过interval，可以执行
                if res - lastTime - 1 > n:
                    res += 1
                else:
                    # 补到距离上一次恰好interval
                    res += n - res + lastTime + 1
            last[t] = res
        return res

test = Solution()
print test.leastInterval(["A","A","A","B","B","B"], 2)