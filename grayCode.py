# -*- coding: utf-8 -*-
# Wikipedia 上的做法就是 01翻转10 然后被加组是 0011（下一个就是000111），变成了 0110 配 0011每一位，就是 00 10 11 01
# https://www.youtube.com/watch?v=P3aCKMMTMCk
class Solution(object):
    def grayCode(self, n):
        res = [0]

        for i in range(n):
            res += [x + pow(2, i) for x in reversed(res)]

        return res