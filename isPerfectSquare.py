class Solution(object):
    def isPerfectSquare(self, num):
        if num < 0:
            return False
        elif num == 0:
            return 0
        low = 1
        high = num
        while low != high - 1:
            mid = (high + low) / 2
            if mid * mid > num:
                high = mid
            elif mid * mid < num:
                low = mid
            if mid * mid == num:
                return True
        return False

test = Solution()
print test.isPerfectSquare(1024)