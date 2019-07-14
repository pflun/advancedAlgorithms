# -*- coding: utf-8 -*-
class Solution(object):
    def multiply(self, num1, num2):
        if not num1 or not num2:
            return
        elif num1 == 0 or num2 == 0:
            return 0

        # 乘数偏移量
        padding = 1
        res = 0

        # 注意从右往左reversed
        for a in num1[::-1]:
            # 被乘数的初始偏移位置
            tens = padding
            for b in num2[::-1]:
                # 每一位两两相乘
                curr = int(a) * int(b) * tens
                res += curr
                # 被乘数偏移量加一
                tens *= 10
            # 乘数偏移量加一位
            padding *= 10

        return str(res)

    def multiply2(self, num1, num2):
        res = 0
        pos = 1

        def helper(num1, n):
            res = 0
            pos = 1
            for n1 in num1[::-1]:
                tmp = int(n1) * int(n)
                res += tmp * pos
                pos *= 10
            return res

        for n in num2[::-1]:
            tmp = helper(num1, n)
            res += tmp * pos
            pos *= 10

        return str(res)

test = Solution()
print test.multiply2('234', '23')
