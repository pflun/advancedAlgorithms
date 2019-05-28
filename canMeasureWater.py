# https://www.cnblogs.com/grandyang/p/5628836.html
class Solution(object):
    def canMeasureWater(self, x, y, z):
        # need a bunch of if to take care corner cases
        if z % self.gcd(x, y) == 0:
            return True
        else:
            return False

    # greatest common divisor
    def gcd(self, x, y):
        if x % y == 0:
            return y
        else:
            return self.gcd(y, x % y)

test = Solution()
print test.canMeasureWater(2, 6, 5)
print test.gcd(3, 5)
