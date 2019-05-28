class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        if x < 0:
            return False
        elif x == 0:
            return 0
        low = 1
        high = x
        while low != high - 1:
            mid = (high + low) / 2
            if mid * mid > x:
                high = mid
            elif mid * mid < x:
                low = mid
            if low == high - 1 or mid * mid == x:
                return mid

test = Solution()
print test.sqrt(63)