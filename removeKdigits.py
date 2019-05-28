# -*- coding: utf-8 -*-
# 找最小的， 规律就是每次都去掉第一个开始递减的数
class Solution(object):
    def removeKdigits(self, num, k):
        for _ in range(k):
            for i in range(len(num) - 1):
                if num[i + 1] > num[i]:
                    num = num[:i + 1] + num[i + 2:]
                    break

        return num

test = Solution()
print test.removeKdigits("1432219", 3)