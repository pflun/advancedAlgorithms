class Solution(object):
    def divide(self, dividend, divisor):
        if dividend > 0:
            op1 = 1
        else:
            op1 = 0
        if divisor > 0:
            op2 = 1
        else:
            op2 = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while dividend - divisor >= 0:
            dividend -= divisor
            res += 1
        return res if op1 == op2 else -res

    # bitwise otherwise TLE
    def divideBit(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)