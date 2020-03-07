import math
class Solution(object):
    def closestDivisors(self, num):
        res1 = self.find2(num + 1)
        res2 = self.find2(num + 2)
        diff1 = abs(res1[0] - res1[1])
        diff2 = abs(res2[0] - res2[1])
        if diff1 < diff2:
            return res1
        else:
            return res2

    def find2(self, x):
        res = [1, x]
        diff1 = abs(res[0] - res[1])
        for n in range(2, x / 2 + 1):
            if x % n == 0:
                another = x / n
                diff2 = abs(n - another)
                if diff2 < diff1:
                    res = [n, another]
                    diff1 = diff2
        return res

    # def find(self, x):
    #     res = [1, x]
    #     low = 1
    #     high = x
    #     while low != high - 1:
    #         mid = (high + low) / 2
    #         if mid * mid > x:
    #             high = mid
    #         elif mid * mid < x:
    #             low = mid
    #         diff1 = abs(res[0] - res[1])
    #         if x % low == 0:
    #             another = x / low
    #             diff2 = abs(low - another)
    #             if diff2 < diff1:
    #                 res = [low, another]
    #         if x % high == 0:
    #             another = x / high
    #             diff2 = abs(high - another)
    #             if diff2 < diff1:
    #                 res = [high, another]
    #         if mid * mid == x:
    #             return [mid, mid]
    #         if low == high - 1:
    #             return res
    #     return res

test = Solution()
print test.closestDivisors(8)
print test.closestDivisors(123)
print test.closestDivisors(999)
print test.closestDivisors(170967091)