# -*- coding: utf-8 -*-
# math.pow( x, y ) （x的y次方）
import math
class Solution(object):
    def titleToNumber(self, s):
        dic = {"A": 1, "B": 2, "C": 3}  # Keep adding D E F ......
        res = 0
        for i in range(len(s)):
            res += dic[s[i]] * math.pow(26, len(s) - i - 1)

        return res

test1 = Solution()
print test1.titleToNumber("ZY")