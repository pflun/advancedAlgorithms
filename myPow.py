class Solution(object):
    # this is for positive n, I'll just need to create a helper func to handle negative
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1.0
        half = n / 2
        if n % 2 == 0:
            sumVal = self.myPow(x, half) * self.myPow(x, half)
        else:
            sumVal = self.myPow(x, half) * x * self.myPow(x, half)

        return sumVal

test = Solution()
print test.myPow(2.00000, -2)