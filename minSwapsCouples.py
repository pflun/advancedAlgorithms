# -*- coding: utf-8 -*-
# https://www.cnblogs.com/grandyang/p/8716597.html
# 暴力换，缺哪个从后面找
class Solution(object):
    def minSwapsCouples(self, row):
        cnt = 0
        for i in range(0, len(row), 2):
            tmp = self.findCouple(row[i])
            if row[i + 1] == tmp:
                continue
            cnt += 1
            for j in range(i + 1, len(row)):
                if row[j] == tmp:
                    row[j], row[i + 1] = row[i + 1], row[j]
                    break
        return cnt

    def findCouple(self, x):
        if x % 2 == 0:
            return x + 1
        elif x % 2 == 1:
            return x - 1

test = Solution()
print test.minSwapsCouples([3,1,4,0,2,5])