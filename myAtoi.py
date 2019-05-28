# -*- coding: utf-8 -*-
import sys
class Solution(object):
    def myAtoi(self, str):
        if len(str) == 0:
            return 0
        str = str.strip()
        # 判断正负号
        sign = 1
        res = 0
        start = 0
        firstChar = str[0]
        if firstChar == '+':
            sign = 1
            start += 1
        elif firstChar == '-':
            sign = -1
            start += 1
        for i in range(start, len(str)):
            if str[i].isdigit():
                res = res * 10 + int(str[i])
                # 越界
                if sign == 1 and res >= sys.maxint:
                    return sys.maxint
                elif sign == -1 and res >= sys.maxint:
                    return -sys.maxint
            else:
                return res * sign

        return res * sign

test = Solution()
print test.myAtoi('  -123454ab  ')